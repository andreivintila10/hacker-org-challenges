import sys

try:
  count = 0
  lastPrime = 2
  with open("primes.txt", "r") as f:
    for line in f:
      if int(line[:-1]) < 1000000000:  
        lastPrime = line[:-1]
        count += 1

finally:
  f.close()
  print(lastPrime)
  print(count)