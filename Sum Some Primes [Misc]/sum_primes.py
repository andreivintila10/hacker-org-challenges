def main():
  count = 2
  sum_prime = 0
  with open("primes.txt", "r") as f:
    for line in f:
      if count >= 49999951 and count <= 50000000:
        prime = int(line[:-1])
        sum_prime += prime
      elif count > 50000000:
        break
      
      count += 1

  #print("There are " + str(count) + " primes in your file");
  print("The sum is: " + str(sum_prime))


if __name__ == '__main__':
  main()