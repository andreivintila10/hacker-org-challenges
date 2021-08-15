#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
//#include <cuda_runtime_api.h>
//#include <cuda.h>
#include <device_launch_parameters.h>
//#include <device_functions.h>
#include "cuda_runtime.h"


cudaError_t decryptWithCuda(unsigned int *four_byte_val);

unsigned int hexadecimalToDecimal(char* hexVal) {
	unsigned short len = strlen(hexVal);
	unsigned int base = 1;
	unsigned int dec_val = 0;

	for (short i = len - 1; i >= 0; i--) {
		if (hexVal[i] >= '0' && hexVal[i] <= '9')
			dec_val += (hexVal[i] - 48) * base;
		else if (hexVal[i] >= 'a' && hexVal[i] <= 'f')
			dec_val += (hexVal[i] - 87) * base;

		base *= 16;
	}

	return dec_val;
}

char* decimalToASCII(unsigned int decimal) {
	unsigned short mask = (1 << 8) - 1;
  //char* string;
  //cudaMallocManaged(&string, sizeof(char) * 5);
	unsigned short byte;
	short i;
	for (i = 3; i >= 0; i--) {
		byte = (decimal >> (i * 8)) & mask;
		if (byte < 32 || byte > 126) {
      //cudaFree(string);
			return NULL;
		}
		//else
			//string[3 - i] = byte;
	}
	//string[4] = '\0';

	return NULL;
}

void decimalToHex(unsigned int decimal) {
	unsigned short mask = (1 << 4) - 1;
	unsigned short byte;
	for (int i = 7; i >= 0; i--) {
		byte = (decimal >> (i * 4)) & mask;
		if (byte < 10)
			byte += 48;
		else if (byte >= 10)
			byte += 87;

		printf("%c", (char)byte);
	}
}


__global__ void decrypt(unsigned int *four_byte_val) {
  unsigned int i = 512 * blockIdx.x + threadIdx.x;
  //unsigned int range = 4294967296;
  //unsigned int range2 = 16777216;
  char *temp;

  char string[185];
  string[184] = '\0';

  unsigned short mask = (1 << 8) - 1;
  char tmp_string[5];
  tmp_string[4] = '\0';

  unsigned int x;
  unsigned int xor;
  unsigned short ok, ok2, count, byte;
  short index, j, k;
  unsigned int left, right;
  left = i * 32768;
  right = (i + 1) * 32768 - 1;
  //printf("Launched thread %u with range (%u, %u)\n", i, left, right);
  for (x = left; x <= right; x++) {
    //printf("%u\n", x);
    count = 180;
    ok = 1;
    for (index = 46; index >= 1; index--) {
      xor = ((four_byte_val[index - 1] + x) % 0x100000000) ^ four_byte_val[index];
      ok2 = 1;
      for (k = 3; k >= 0; k--) {
        byte = (xor >> (k * 8)) & mask;
        if (byte < 32 || byte > 126) {
          ok2 = 0;
          break;
        }
        else {
          tmp_string[3 - k] = (char)byte;
        }
      }
      
      if (ok2 == 1) {
        for (j = count; j < count + 4; j++)
          string[j] = tmp_string[j % 4];
        count -= 4;
      }
      else {
        ok = 0;
        break;
      }
    }

    if (ok == 1) {
      //fprintf(fp, "%s\n", string);
      printf("%ld %s\n", x, string);
    }

    if (x == 4294967295)
      break;
    //printf("HERE %d\n", i);
  }
  //printf("EXITED %u\n", i);
}


int main() {
  time_t seconds = time(NULL);
	char *ciphertext = "5499fa991ee7d8da5df0b78b1cb0c18c10f09fc54bb7fdae7fcb95ace494fbae8f5d90a3c766fdd7b7399eccbf4af592f35c9dc2272be2a45e788697520febd8468c808c2e550ac92b4d28b74c16678933df0bec67a967780ffa0ce344cd2a9a2dc208dc35c26a9d658b0fd70d00648246c90cf828d72a794ea94be51bbc6995478505d37b1a6b8daf7408dbef7d7f9f76471cc6ef1076b46c911aa7e75a7ed389630c8df32b7fcb697c1e89091c30be736a4cbfe27339bb9a2a52a280";
  char *substr = (char *) malloc(sizeof(char) * 9);
  unsigned int *four_byte_val = (unsigned int *) malloc(sizeof(unsigned int) * 47);
  substr[8] = '\0';

  short i = 46;
  for (short index = strlen(ciphertext) - 10; index >= 0; index -= 8) {
    strncpy(substr, ciphertext + index, 8);
    four_byte_val[i--] = hexadecimalToDecimal(substr);
  }

  free(substr);
  for (size_t p = 0; p < 47; p++)
    printf("%u\n", four_byte_val[p]);

  free(four_byte_val);
  //FILE * fp = fopen("decrypt.txt", "w+");
  
  // Add vectors in parallel.
  cudaError_t cudaStatus = decryptWithCuda(four_byte_val);
  if (cudaStatus != cudaSuccess) {
    fprintf(stderr, "decryptWithCuda failed!");
    return 1;
  }

  cudaStatus = cudaDeviceReset();
  if (cudaStatus != cudaSuccess) {
    fprintf(stderr, "cudaDeviceReset failed!");
    return 1;
  }

	//fclose(fp);
  printf("Program finished in %d seconds\n", (time(NULL) - seconds));

	return 0;
}

cudaError_t decryptWithCuda(unsigned int *four_byte_val) {
  unsigned int* dev_four_byte_val = NULL;
  cudaError_t cudaStatus;

  // Choose which GPU to run on, change this on a multi-GPU system.
  cudaStatus = cudaSetDevice(0);
  if (cudaStatus != cudaSuccess) {
    fprintf(stderr, "cudaSetDevice failed! Do you have a CUDA-capable GPU installed?");
    goto Error;
  }

  // Allocate GPU buffers for three vectors (two input, one output).
  cudaStatus = cudaMalloc((void**)&dev_four_byte_val, 47 * sizeof(unsigned int));
  if (cudaStatus != cudaSuccess) {
    fprintf(stderr, "cudaMalloc failed!");
    goto Error;
  }

  // Copy input vectors from host memory to GPU buffers.
  cudaStatus = cudaMemcpy(dev_four_byte_val, four_byte_val, 47 * sizeof(unsigned int), cudaMemcpyHostToDevice);
  if (cudaStatus != cudaSuccess) {
    fprintf(stderr, "cudaMemcpy failed!");
    goto Error;
  }

  // Launch a kernel on the GPU with one thread for each element.
  decrypt<<<512, 256>>>(dev_four_byte_val);

  // Check for any errors launching the kernel
  cudaStatus = cudaGetLastError();
  if (cudaStatus != cudaSuccess) {
    fprintf(stderr, "decryptKernel launch failed: %s\n", cudaGetErrorString(cudaStatus));
    goto Error;
  }

  // cudaDeviceSynchronize waits for the kernel to finish, and returns
  // any errors encountered during the launch.
  cudaStatus = cudaDeviceSynchronize();
  if (cudaStatus != cudaSuccess) {
    fprintf(stderr, "cudaDeviceSynchronize returned error code %d after launching decryptKernel!\n", cudaStatus);
    goto Error;
  }

Error:
  cudaFree(dev_four_byte_val);

  return cudaStatus;
}