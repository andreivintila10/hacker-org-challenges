import sys

cipher_text_hex = "948881859781c4979186898d90c4c68c85878f85808b8b808881c6c4828b96c4908c8d97c4878c858888818a8381"


def printChar():
  return 0

for key_dec in range(256):
  string = ""
  for index in range(number_of_bytes):
    left = index * 2
    right = left + 2
    xor = int(cipher_text_hex[left:right], 16) ^ key_dec
    if xor < 32 or xor > 126:
      break;

    string += str(chr(xor))
  print(string)