import sys


def main():
  words = []
  with open("text.txt", "r") as f:
    for line in f:
      if line[-1] == '\n':
        line = line[:-1]
      for word in line.split():
        cleanWorld = ""
        for char in word:
          if char in ",./;:\'\"\\[]{}|`~!@#$%^&*()_+-=<>?":
            char = " "

          cleanWorld += char

        newWords = cleanWorld.split()
        if len(newWords) < 1 or len(newWords) > 1:
          print(' '.join(newWords))

        for word_ in newWords:
          words.append(word_.lower())

  print(' '.join(words))
  binary_string = ""
  count = 0
  for word in words:
    if word == "she" != -1 or word == "her" != -1 or word == "herself":
      binary_string += "1"
      count += 1
    elif word == "he" != -1 or word == "his" != -1 or word == "him" or word == "himself":
      binary_string += "0"
      count += 1

    # if word.find("she") != -1 or word.find("her") != -1:
    #   binary_string += "0"
    #   count += 1
    # elif word.find("he") != -1 or word.find("him") != -1:
    #   binary_string += "1"
    #   count += 1

  print(len(binary_string))
  print(binary_string)
  left = 0
  right = left + 8
  for index in range(int(len(binary_string) / 8)):
    sys.stdout.write(str(chr(int(binary_string[left:right], 2))))
    left = right
    right += 8
  # for pos in range(number_of_bytes):
  #   byte = int(binary_string[left:right], 2)
  #   sys.stdout.write(str(chr(byte)))
  #   left = right
  #   right += 8



main()