def get_xor(a, b):
  return a ^ b


def get_printable_chars(hex_val):
  values = []
  for val in range(256):
    xor = get_xor(val, int(hex_val, 16))
    if xor >= 32 and xor <= 126:
      values.append(val)

  print("Starting key byte values: " + str(len(values)))     

  return values



def main():
  try:
    cipher_text = "31cf55aa0c91fb6fcb33f34793fe00c72ebc4c88fd57dc6ba71e71b759d83588"
    number_of_bytes = int(len(cipher_text) / 2)
    values = get_printable_chars(cipher_text[0:2])
    f = open("decode.txt", "w")
    for b in range(256):
      currentByte = b
      for x in range(256):
        string = ""
        for index in range(number_of_bytes):
          left = index * 2
          right = left + 2
          xor = get_xor(int(cipher_text[left:right], 16), currentByte)
          currentByte = (currentByte + x) % 256

          if xor < 32 or xor > 126:
            string += " "
          else:
            string += str(chr(xor))
        
        f.write(string + "\n")

  finally:
    f.close()


main()