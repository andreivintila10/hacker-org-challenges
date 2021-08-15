import sys


def main():
  #first 35 bytes are valid, rest are corupt
  cipher_text = "8d541ae26426f8b97426b7ae7240d78e401f8f904717d09b2fa4a4622cfcbf7337fbba020cdbcb4e3cdb994812b66a27e9e02f21faf8712bd290070fc384560490988507e3b1"
  cipher_text2 = "020cdbcb4e3cdb994812b66a27e9e02f21faf8712bd2907fc384564998857e3b1"
  print("Bytes: " + str(len(cipher_text) / 2))
  number_of_bytes = int(len(cipher_text) / 2)
  number_of_bytes2 = int(len(cipher_text2) / 2)
  string = "the answer to this broken challenge  c   - (  $ i . m 0 1         "
  byte_key = 249
  special_x = 67
  currentByte = byte_key
  for index in range(number_of_bytes):
    left = index * 2
    right = left + 2
    result = currentByte ^ int(cipher_text[left:right], 16)
    currentByte = (currentByte + special_x) % 256
    if result < 32 or result > 126:
      result = 34
    sys.stdout.write(str(chr(result)))

  print("")
  byte35 = cipher_text[68:70]
  currentByte = byte_key
  for index in range(34):
    currentByte = (currentByte + special_x) % 256
  result = currentByte ^ int(byte35, 16)
  print(str(chr(result)) + " " + str(result))


main()