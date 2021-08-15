#include <stdio.h>
#include <string.h>


long long int hexadecimalToDecimal(char *hexVal) {
  int len = strlen(hexVal);

  long long int base = 1;
  long long int dec_val = 0;

  for (int i = len - 1; i >= 0; i--)
    if (hexVal[i] >= '0' && hexVal[i] <= '9') {
      dec_val += (hexVal[i] - 48) * base;
      base *= 16;
    }
    else if (hexVal[i] >= 'a' && hexVal[i] <= 'f') {
      dec_val += (hexVal[i] - 87) * base;
      base *= 16;
    }

  return dec_val;
}

char decimalToASCII(int decimal) {
  if (decimal < 32 || decimal > 126)
    return NULL;
  else
    return (char) decimal;
}

void decimalToHex(long long int decimal) {
  long long int mask = (1 << 4) - 1;
  char string[8];
  int byte;
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
  char *ciphertext = "310a7718781f734c31425e775a314f3b40132c5122720599b2dfb790fd8ff894add2a4bdc5d1a6e987a0ed8eee94adcfbb94ee88f382127819623a404d3f";
  int ciphertext_length = strlen(ciphertext);
  printf("%s\n", ciphertext);
  printf("Length: %i\n", ciphertext_length);

  int keys[95];
  int i = 0;
  int byte = hexadecimalToDecimal("4d");
  int byte2 = hexadecimalToDecimal("3f");
  int result;
  for (int x = 0; x < 256; x++) {
    result = ((byte + x) % 256) ^ byte2;
    if (result >= 32 && result <= 126) {
      keys[i] = x;
      // printf("%i\n", x);
      i++;
    }
  }

  char *substr = (char *) malloc(sizeof(char) * 3);
  char *substr2 = (char *) malloc(sizeof(char) * 3);
  char string[strlen(ciphertext) / 2];

  for (int var = 0; var < 95; var++) {
    int ok = 1;
    int count = strlen(ciphertext) / 2 - 2;
    for (int index = ciphertext_length - 1; index >= 2; index -= 2) {
      strncpy(substr, ciphertext + index - 1, 2);
      strncpy(substr2, ciphertext + index - 3, 2);
      substr[2] = '\0';
      substr2[2] = '\0';

      int xor = ((hexadecimalToDecimal(substr2) + keys[var]) % 256) ^ hexadecimalToDecimal(substr);

      char temp = decimalToASCII(xor);
      if (temp == NULL) {
        ok = 0;
        printf("\n");
        break;
      }
      else {
        string[count] = temp;
        printf("%c", temp);
        count -= 1;
      }
    }

    if (ok == 1) {
      string[strlen(ciphertext) / 2 - 1] = '\0';
      printf("%s\n", string);
    }
  }

  return 1;
}
