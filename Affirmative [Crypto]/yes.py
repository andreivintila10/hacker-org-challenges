def main():
  string = "";

  with open("text.txt", "r") as f:
    for line in f:
      for word in line.split():
        char = str(chr(int(word, 16)));
        if char.islower():
          string += "0";
        elif char.isupper():
          string += "1";
        else:
          string += char;

  print(string);


if __name__ == '__main__':
    main()