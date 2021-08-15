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

char *decimalToASCII(long long int decimal) {
  long long int mask = (1 << 8) - 1;
  char *string = (char *) malloc(sizeof(char) * 5);
  int byte;
  for (int i = 3; i >= 0; i--) {
    byte = (decimal >> (i * 8)) & mask;
    //printf("%c", (char) byte);
    string[3 - i] = (char) byte;
  }
  string[4] = '\0';

  //printf("Decimal %lli to ASCII is: %s\n", decimal, string);

  return string;
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
  // printf("%c\n", (char) 119);
  /*int b1, b2, b3, b4;
  for (b1 = 0; b1 < 256; b1++) {
    for (b2 = 0; b2 < 256; b2++) {
      for (b3 = 0; b3 < 256; b3++) {
        for (b4 = 0; b4 < 256; b4++) {
          count++;
        }
      }
    }
  }
  printf("Count: %lli", count); */

  char *ciphertext = "e5534adac53023aaad55518ac42671f8a1471d94d8676ce1b11309c1c27a64b1ae1f4a91c73f2bfce74c5e8e826c27e1f74c4f8081296ff3ee4519968a6570e2aa0709c2c4687eece44a1589903e79ece75117cec73864eebe57119c9e367fefe9530dc1";
  int ciphertext_length = strlen(ciphertext);
  printf("%s\n", ciphertext);
  // printf("%i\n", ciphertext_length);
  int index;
  char *substr = (char *) malloc(sizeof(char) * 9);
  char *substr2 = (char *) malloc(sizeof(char) * 9);
  char string[97];
  int count = 92;
  char *temp = (char*) malloc(sizeof(char) * 5);
  for (index = ciphertext_length - 1; index >= 8; index -= 8) {
    strncpy(substr, ciphertext + index - 7, 8);
    strncpy(substr2, ciphertext + index - 15, 8);
    long long int xor = hexadecimalToDecimal(substr2) ^ hexadecimalToDecimal(substr);
    strcpy(temp, decimalToASCII(xor));
    //printf("%s\n", temp);
    for (int j = count; j < count + 4; j++)
      string[j] = temp[(size_t) (j % 4)];
    count -= 4;
    //printf("%s\n", temp);
    // printf("%s\t%lli\t\t%s\t%lli\n", substr2, hexadecimalToDecimal(substr2), substr, hexadecimalToDecimal(substr));
    // printf("%s\n", hexadecimalToDecimal(strcpy(ciphertext + index - 8, ciphertext + index)));
  }
  string[96] = '\0';
  printf("%s", string);

  // decimalToHex(3914534337);
  return 1;
}
