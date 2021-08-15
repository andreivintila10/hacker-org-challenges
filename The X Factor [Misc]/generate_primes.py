from math import sqrt
from math import ceil
# from BigNumber import BigNumber
from time import time


def sieve_of_eratostene(length, sqrt_length):
  index = 0
  sieve = [True] * length
  sieve[0] = sieve[1] = False
  lastPrime = 2
  primes = []

  try:
    f = open("primes.txt", "w")
    for index in range(3, sqrt_length + 1, 2):
      if sieve[index]:
        # lastPrime = index
        # print(index)
        f.write(str(index) + '\n')
        primes.append(index)
        for index2 in range(index * index, length, index + index):
          sieve[index2] = False

  finally:
    # index += 1
    # # print(str(index) + " " + str(sqrt_length))
    # if index != sqrt_length:
    #   index = lastPrime

    for index2 in range(sqrt_length + 1 + (sqrt_length % 2), length, 2):
      if sieve[index2]:
        # print(index2)
        f.write(str(index2) + '\n')
        primes.append(index2)

    f.close()
    # print("Generated primes up to " + str(index2 + (index2 % 2)) + "/" + str(length - 1) + " in: " + str(ceil(time() - t)) + " seconds")
    return primes


def sieve_of_eratostene2(length, sqrt_length, sqrt_length2):
  t = time()
  try:
    f = open("primes.txt", "a+")
    primes = sieve_of_eratostene(sqrt_length, sqrt_length2)
    # bg_zero = BigNumber("0")
    low = sqrt_length
    high = low + sqrt_length
    for index in range(1, sqrt_length):
      print(index)
      # bg_low = BigNumber(low)
      sieve = [True] * sqrt_length
      for prime in primes:
        start = prime * prime
        if start < low:
          # bg_prime = BigNumber(prime)
          # bg_mod = bg_low.mod(bg_prime)
          # diff = prime - bg_mod.convertToDecimal()
          diff = (prime - (low % prime)) % prime
          start = low + diff
          start += ((start + 1) % 2) * prime
        elif start >= high:
          break
        # print(str(low) + " " + str(high) + " " + str(start) + " " + str(prime))
        for index2 in range(start, high, prime + prime):
          sieve[index2 - low] = False

      for index2 in range((low + 1) % 2, sqrt_length, 2):
        if sieve[index2]:
          # print(index2 + low)
          f.write(str(index2 + low) + '\n')
          primes.append(index2 + low)

      low = high
      high += sqrt_length

  finally:
    f.close()
    print("Generated primes up to " + str(length) + " in: " + str(ceil(time() - t)) + " seconds")

def main():
  # number_string = "7393913335919140050521110339491123405991919445111971"
  # index = BigNumber(3)
  # zero = BigNumber(0)
  # increment = BigNumber(2)
  # bg_number = BigNumber(number_string)
  # while index.minus(bg_number).isNegative():
  #   while bg_number.mod(index).equals(zero):
  #     bg_number = bg_number.divide(index)
  #     print(index.toString() + " " + bg_number.toString())

  #   index = index.plus(increment)
  
  test_length = 100000000
  sqrt_test_length = 10000
  number_length = 27940728383767010155483
  sqrt_number_length = 167154803651
  max_length = 3049800625
  sqrt_max_length = 55225
  sqrt_max_length2 = 234
  sieve_of_eratostene2(max_length, sqrt_max_length, sqrt_max_length2)
  # prime_numbers = []
  # count = 0
  # for isPrime in sieve:
  #   if isPrime:
  #     sys.stdout.write(str(count) + " ")
  #     prime_numbers.append(count)
  #   count += 1


main()