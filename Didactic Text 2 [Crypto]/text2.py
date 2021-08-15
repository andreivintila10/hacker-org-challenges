import sys

def char_code(code):
  characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  return characters[code]

char_array = [8, 4, 20, 9, 21, 14, 26, 15, 31, 19, 32, 15, 1, 18, 24, 5, 24, 1, 33, 19, 28, 19]
char_array2 = [8, 4, 2, 0, 9, 2, 1, 1, 4, 2, 6, 1, 5, 3, 1, 1, 9, 3, 2, 1, 5, 1, 1, 8, 2, 4, 5, 2, 4, 1, 3, 3, 1, 9, 2, 8, 1, 9]
char_array3 = [4, 9, 14, 15, 19, 15, 18, 5, 1, 19, 19]

for character in char_array3:
	sys.stdout.write(char_code((character - 1) % 26))