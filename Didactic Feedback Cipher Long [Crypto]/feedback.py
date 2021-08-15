def main():
  cipher_text = "e5534adac53023aaad55518ac42671f8a1471d94d8676ce1b11309c1c27a64b1ae1f4a91c73f2bfce74c5e8e826c27e1f74c4f8081296ff3ee4519968a6570e2aa0709c2c4687eece44a1589903e79ece75117cec73864eebe57119c9e367fefe9530dc1"
  number_of_bytes = int(len(cipher_text) / 2)

  string = ""
  for index in range(number_of_bytes - 1, -1, -8):
    left1 = (number_of_bytes - index - 1) * 2 - 2
    right1 = left1 + 2
    left2 = (number_of_bytes - index - 1) * 2
    right2 =  left2 + 2

    c = int(cipher_text[left1:right1], 16) ^ int(cipher_text[left2:right2], 16)
    string = str(chr(c)) + string
  print(string)


main()