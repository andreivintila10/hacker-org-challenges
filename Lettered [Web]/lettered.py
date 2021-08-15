def main():
  text = "&#38&#119&#101&#105&#101&#114&#112&#59&#38&#79&#116&#105&#108&#100&#101&#59&#38&#85&#103&#114&#97&#118&#101&#59&#38&#114&#101&#97&#108&#59&#38&#99&#111&#112&#121&#59&#38&#84&#104&#101&#116&#97&#59&#38&#102&#110&#111&#102&#59&#38&#102&#110&#111&#102&#59&#38&#105&#115&#105&#110&#59&#38&#105&#115&#105&#110&#59"
  index = 0
  length = len(text)
  string = ""
  while index < length:
    if text[index:index+2] == "&#":
      index += 2
    else:
      index2 = index + 1
      while index2 < length and text[index2].isdigit():
        index2 += 1
      string += str(chr(int(text[index:index2])))
      index = index2

  print(string)

main()