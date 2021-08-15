import sys

cipher_text_hex = "8776459cf37d459fbb7b5ecfbb7f5fcfb23e478aaa3e4389f378439aa13e4e96a77b5fc1f358439df36a4486a03e4381b63e5580a66c0c8ebd6d5b8aa13e459cf34e4d9fa67f02cf90714288a17f589abf7f5886bc705fcfbc700c96bc6b5ecfb7775f8cbc68499daa3f"
number_of_bytes = int(len(cipher_text_hex) / 2)

byte0_values = []
byte1_values = []
byte2_values = []
byte3_values = []
for index in range(256):
  xor = int(cipher_text_hex[0:2], 16) ^ index
  if xor >= 32 and xor <= 126:
    byte0_values.append(index)

  xor = int(cipher_text_hex[2:4], 16) ^ index
  if xor >= 32 and xor <= 126:
    byte1_values.append(index)

  xor = int(cipher_text_hex[4:6], 16) ^ index
  if xor >= 32 and xor <= 126:
    byte2_values.append(index)

  xor = int(cipher_text_hex[6:8], 16) ^ index
  if xor >= 32 and xor <= 126:
    byte3_values.append(index)

byte0_total_values = len(byte0_values)
byte1_total_values = len(byte1_values)
byte2_total_values = len(byte2_values)
byte3_total_values = len(byte3_values)
TOTAL_VALUES = byte0_total_values * byte1_total_values * byte2_total_values * byte3_total_values
print("BYTE1_TOTAL_VALUES: " + str(byte0_total_values))
print("BYTE2_TOTAL_VALUES: " + str(byte1_total_values))
print("BYTE3_TOTAL_VALUES: " + str(byte2_total_values))
print("BYTE4_TOTAL_VALUES: " + str(byte3_total_values))
print("TOTAL VALID CHECKS: " + str(TOTAL_VALUES))


try:
  f = open("decoded.txt", "w")
  strings = []
  bytes_array_dec = [0, 0, 0, 0]
  for index0 in range(byte0_total_values):
    bytes_array_dec[0] = byte0_values[index0]
    for index1 in range(byte1_total_values):
      bytes_array_dec[1] = byte1_values[index1]
      for index2 in range(byte2_total_values):
        bytes_array_dec[2] = byte2_values[index2]
        for index3 in range(byte3_total_values):
          bytes_array_dec[3] = byte3_values[index3]
          string = ""
          ok = 1
          for index in range(int(number_of_bytes / 4)):
            for index2 in range(4):
              left = (index * 4 + index2) * 2
              right = left + 2
              xor = int(cipher_text_hex[left:right], 16) ^ bytes_array_dec[index2]
              #print("XOR OF " + str(int(cipher_text_hex[left:right], 16)) + " WITH " + str(bytes_array_dec[index2]) + " IS " + str(xor) + " | BYTE1: " + str(byte0_key_dec) + " BYTE2: " + str(byte1_key_dec) + " BYTE3: " + str(byte2_key_dec) + " BYTE4: " + str(byte3_key_dec))
              if xor < 32 or xor > 126:
                ok = 0
                break;

              string += str(chr(xor))

            if ok == 0:
              break

          if ok == 1:
            f.write(string + "\n")

finally:
  f.close()