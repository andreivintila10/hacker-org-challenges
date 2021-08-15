import sys


def power(base, exponent):
  result = index = 1
  while index <= exponent:
    result *= base
    index += 1

  return result


def main():
  a = 17
  b = 39
  c = 11
  result = power(17, 39)
  result = power(result, 11)
  result_string = str(result)
  print("Result is: " + str(result))
  print("Every 33rd digits are: ")
  for index in range(len(result_string)):
    if index % 33 == 0:
      sys.stdout.write(result_string[index])


main()