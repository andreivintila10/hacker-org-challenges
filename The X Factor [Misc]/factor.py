from BigNumber import BigNumber
from time import time


def main():
  t = time()
  try:
    primes = []
    with open("primes.txt") as f:
      primes = [line.rstrip('\n') for line in f]

    bg_number = BigNumber("7393913335919140050521110339491123405991919445111971")
    bg_zero = BigNumber(0)
    for prime in reversed(primes):
      bg_prime = BigNumber(prime)
      while bg_number.mod(bg_prime).equals(bg_zero):
        bg_number = bg_number.divide(bg_prime)
        print(bg_prime.toString() + "\t" + bg_number.toString())

  finally:
    f.close()
    print("Checked primes in: " + str(ceil(time() - t)) + " seconds")


main()