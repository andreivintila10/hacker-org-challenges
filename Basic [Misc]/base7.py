from BigNumber import BigNumber


def multiply_with_one_digit(this_list, digit):
  number = [*this_list]

  carry = 0
  for index, num_digit in reversed(list(enumerate(number))):
    digit_mult = num_digit * digit + carry
    number[index] = digit_mult % 10
    carry = int(digit_mult / 10)

  if carry > 0:
    number.insert(0, carry)

  while len(number) > 1 and number[0] == 0:
    del number[0]

  return number


def main():
  powers = [0] * 100
  bg_number = BigNumber("167")
  bg_number2 = BigNumber("28679718602997181072337614380936720482949")
  number2 = 167
  number = 28679718602997181072337614380936720482949
  bg_zero = BigNumber("0")
  bg_one = BigNumber("1")
  bg_seven = BigNumber("7")
  while number > 0:
    count = 0
    temp = 1
    while temp * 7 <= number:
      temp *= 7
      count += 1

    index = 0
    while temp * (index + 1) <= number:
      index += 1

    powers[count] = index
    number -= (temp * index)
    print(str(count) + " " + str(powers[count]))

  i = 99
  while i >= 0 and powers[i] == 0:
    i -= 1

  string = ""
  for index in range(i, -1, -1):
    string += str(powers[index])

  print(string)


main()