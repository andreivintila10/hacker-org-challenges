#include <stdio.h>
#include <string.h>
#include <stdlib.h>


unsigned int hexadecimalToDecimal(char *hexVal) {
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

char *decimalToASCII(unsigned int decimal) {
  unsigned short mask = (1 << 8) - 1;
  char *string = (char *) malloc(sizeof(char) * 5);
  unsigned short byte;
  short i;
  for (i = 3; i >= 0; i--) {
    byte = (decimal >> (i * 8)) & mask;
    if (byte < 32 || byte > 126) {
      free(string);
      return NULL;
    }
    else
      string[3 - i] = (char) byte;
  }
  string[4] = '\0';

  return string;
}

void decimalToHex(unsigned int decimal) {
  unsigned short mask = (1 << 4) - 1;
  char string[8];
  unsigned short byte;
  for (int i = 7; i >= 0; i--) {
    byte = (decimal >> (i * 4 )) & mask;
    if (byte < 10)
      byte += 48;
    else if (byte >= 10)
      byte += 87;

    printf("%c", (char) byte);
  }
}


int main() {
  char *ciphertext = "5499fa991ee7d8da5df0b78b1cb0c18c10f09fc54bb7fdae7fcb95ace494fbae8f5d90a3c766fdd7b7399eccbf4af592f35c9dc2272be2a45e788697520febd8468c808c2e550ac92b4d28b74c16678933df0bec67a967780ffa0ce344cd2a9a2dc208dc35c26a9d658b0fd70d00648246c90cf828d72a794ea94be51bbc6995478505d37b1a6b8daf7408dbef7d7f9f76471cc6ef1076b46c911aa7e75a7ed389630c8df32b7fcb697c1e89091c30be736a4cbfe27339bb9a2a52a280";
  unsigned short ciphertext_length = strlen(ciphertext);
  printf("%s\n", ciphertext);
  printf("%d\n", ciphertext_length);
  char *substr = (char *) malloc(sizeof(char) * 9);
  char *substr2 = (char *) malloc(sizeof(char) * 9);
  char *temp;

  char string[185];
  string[184] = '\0';

  unsigned int x;
  unsigned int xor;
  unsigned short mask = (1 << 8) - 1;
  unsigned short ok, count;
  short index, j;
  unsigned int max_int = 4294967295;
  FILE *fp = fopen("decrypt.txt", "w+");
  for (x = 0; x <= max_int; x++) {
    count = 180;
    ok = 1;
    for (index = ciphertext_length - 3; index >= 8; index -= 8) {
      strncpy(substr, ciphertext + index - 7, 8);
      strncpy(substr2, ciphertext + index - 15, 8);
      substr[8] = '\0';
      substr2[8] = '\0';
      xor = ((hexadecimalToDecimal(substr2) + x) % 0x100000000) ^ hexadecimalToDecimal(substr);
      temp = decimalToASCII(xor);
      if (temp != NULL) {
        temp[4] = '\0';
        for (j = count; j < count + 4; j++)
          string[j] = temp[(size_t) (j % 4)];
        count -= 4;
        free(temp);
      }
      else {
        ok = 0;
        break;
      }
    }

    if (ok == 1) {
      fprintf(fp, "%s\n", string);
      printf("%s\n", string);
    }

    if (x == max_int)
      break;
  }
  printf("%u\n", x);
  fclose(fp);

  return 1;
}