import gzip
import urllib.request


def main():
  content = urllib.request.urlopen('http://www.hacker.org/challenge/img/someimage.sgi').read()
  try:
    content = gzip.decompress(content)

  except:
    print("Cannot decompress");

  print(content);


main()