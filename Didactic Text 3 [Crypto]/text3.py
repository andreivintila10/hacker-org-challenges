import sys


def main():
  spaces = []
  with open("webpage.txt") as f:
    for line in f:
      if line[len(line) - 1] == '\n':
        line = line[:-1]

      count = 0
      while len(line) > 0 and line[len(line) - 1] == ' ':
        count += 1
        line = line[:-1]

      spaces.append(str(int(count / 2)))

  spaces[len(spaces) - 1] = "1"
  print(spaces[-1])
  number_of_bytes = int(len(spaces) / 8)
  binary_string = ''.join(spaces)
  left = 0
  right = 8
  for pos in range(number_of_bytes):
    byte = int(binary_string[left:right], 2)
    sys.stdout.write(str(chr(byte)))
    left = right
    right += 8


main()