import sys


def main():
  text = "it$aeihea siibea nahxpasriweA m2ao2aahielhxpanA114."
  decoded = set()
  for letter in text:
    decoded.update(letter)
  print(''.join(decoded))
  for c in decoded:
    sys.stdout.write(c)
    o=''.join([ c if c==x else ' ' for x in text])
    print(o)


main()