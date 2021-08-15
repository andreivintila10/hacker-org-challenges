import gzip
import urllib.request


def main():
  content = urllib.request.urlopen('http://www.hacker.org/challenge/misc/doll.bin').read()
  print(content.decode())
  count = 0

  while True:
    try:
      content = gzip.decompress(content)
      count += 1

    except:
      break

  print(content)
  print(count)
  print(content.decode())


if __name__ == '__main__':
  main()