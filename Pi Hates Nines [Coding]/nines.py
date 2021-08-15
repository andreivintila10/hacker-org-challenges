def main():
  count = 0
  longest_sequence = ""
  longest_sequence_length = 0
  current_sequence = ""
  with open("pi1000000.txt") as f:
    byte = f.read(1)
    while byte:
      # if not byte.isdigit():
      #   print(byte + "  " + str(ord(byte)) + "  " + str(count))

      count += 1
      if byte == '9':
        if longest_sequence_length < len(current_sequence):
          longest_sequence = current_sequence
          longest_sequence_length = len(current_sequence)
        current_sequence = ""
      else:
        current_sequence += byte

      byte = f.read(1)

  if len(current_sequence) > longest_sequence_length:
    longest_sequence = current_sequence

  f = open("longest_sequence.txt", "w")
  f.write(longest_sequence)
  f.close()
  # print("Longest sequence: " + longest_sequence)
  # print("Count: " + str(count))


main()