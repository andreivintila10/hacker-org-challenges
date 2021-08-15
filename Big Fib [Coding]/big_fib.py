import sys
import math
from decimal import Decimal


def main():
  prev = 0
  curr = 1
  for index in range(2, 150000001):
    temp = curr
    curr += prev
    prev = temp

  print(curr)
  curr = math.log(curr)
  print(curr)
  curr = round(curr, 3)
  print(curr)
  # string_curr = str(curr)
  # count = 0
  # for digit in string_curr:
  #   if count % 20000 == 0:
  #     sys.stdout.write(digit)
  #   count += 1


if __name__ == '__main__':
  main()