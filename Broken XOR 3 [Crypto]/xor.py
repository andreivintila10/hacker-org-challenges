def get_xor(a, b):
  return a ^ b


def main():
  try:
    cipher_text = "8d541ae26426f8b97426b7ae7240d78e401f8f904717d09b2fa4a4622cfcbf7337fbba2cdbcb4e3cdb994812b66a27e9e02f21faf8712bd2907fc384564998857e3b1"
    number_of_bytes = int(len(cipher_text) / 2)
    print(str(number_of_bytes))
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
        
        f.write(string + "  " + str(b) + " " + str(x) + "\n")

  finally:
    f.close()


main()