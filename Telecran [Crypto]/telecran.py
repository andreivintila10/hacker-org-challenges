import sys
from PIL import Image


def printMatrix(matrix):
  for index in range(100):
  	for index2 in range(100):
  	  sys.stdout.write(str(matrix[index][index2]))
  	print("")


# with open("directions.txt", "r") as f:
# 	for line in f:
# 		directions = line

directions = ""
with open("flags.txt", "r") as f:
	for line in f:
		print(line)
		if line == "ro\n":
			directions += 'r'
		elif line == "lu\n":
		  directions += 'l'
		elif line == "dk\n":
		  directions += 'd'
		elif line == "ua\n":
		  directions += 'u'

print(directions)

matrix = []
n = 100
matrix = [[' '] * n for i in range(n)]

originX = 20
originY = 50
matrix[originY][originX] = '.'

out_image = Image.new('1', (300, 30))
x, y = 10, 10
out_image.putpixel((x, y), 1)

for index in range(len(directions)):
  for _ in range(5):
    if directions[index] == 'd':
      originY += 1
      y += 1
      #matrix[originY][originX] = '|'
    elif directions[index] == 'u':
      originY -= 1
      y -= 1
      #matrix[originY][originX] = '|'
    elif directions[index] == 'l':
      originX -= 1
      x -= 1
      #matrix[originY][originX] = '_'
    elif directions[index] == 'r':
      originX += 1
      x += 1
      #matrix[originY][originX] = '_'
    #matrix[originY][originX] = '.'
    out_image.putpixel((x, y), 1)

printMatrix(matrix)
out_image.show()
out_image.close()