import sys


def main():
  try:
    currentSequence = [0] * 8
    match = ["1", "2", "3", "4", "5", "6", "7", "8"]
    count = -1
    with open("Pi - Dec - Chudnovsky.txt", "r") as f:
      for index in range(8):
        currentSequence[index] = str(f.read(1))
        count += 1

      byte = str(f.read(1))
      while currentSequence != match and byte:
        currentSequence = currentSequence[1:]
        currentSequence.append(str(byte))
        # print(''.join(currentSequence))
        count += 1
        byte = f.read(1)

    print(str(count - 8) + " " + ''.join(currentSequence))

  finally:
    f.close()

  # print(string[0] + " " + str(len(string)))
  # match = "12345678"
  # match2 = "52521385"
  # len_match = len(match)
  # for index in range(0, len(string) - len_match + 1):
  #   # print(string[index:index + len_match])
  #   if string[index:index + len_match] == match:
  #     print("Position: " + str(index - 1))
  #     break


main()