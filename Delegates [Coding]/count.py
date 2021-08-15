from math import sqrt
import sys

n = 2118
total = int((n * (n + 1)) / 2)

no_of_squares = int(sqrt(n)) + 1
for index in range(no_of_squares):
  square = index * index
  total += square
  #sys.stdout.write(square + " ")

print("Total: " + str(total))