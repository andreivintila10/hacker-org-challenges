def main():
  number1 = 0 
  number2 = 1
  index = 1
  sumFib = 0
  while index <= 17:
    if index >= 10:
      sumFib += number2 
    temp = number1 + number2
    number1 = number2
    number2 = temp
    index += 1

  print("Sum is: " + str(sumFib))


main()