def main():
  cipher_text = "751a6f1d3d5c3241365321016c05620a7e5e34413246660461412e5a2e412c49254a24"
  number_of_half_bytes = len(cipher_text)
  number_of_bytes = int(number_of_half_bytes / 2)

  string = ""
  for index in range(number_of_bytes - 1):
    left1 = (number_of_bytes - index - 1) * 2 - 2
    right1 = left1 + 2
    left2 = (number_of_bytes - index - 1) * 2
    right2 =  left2 + 2

    c = int(cipher_text[left1:right1], 16) ^ int(cipher_text[left2:right2], 16)
    string = str(chr(c)) + string
  print(string)


main()