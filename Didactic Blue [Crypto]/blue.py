import sys
from PIL import Image

im = Image.open('blue.png')
rgb_im = im.convert('RGB')
width, height = im.size
blue = []
binary_string = ""
for index in range(height):
  for index2 in range(width):
    r, g, b = rgb_im.getpixel((index2, height - index - 1))
    #print(str(r) + " " + str(g) + " " + str(b))
    blue.append(b);
    binary_string += '{0:08b}'.format(b)[7]

for index in range(48):
  left = index * 8
  right = left + 8
  byte_int = int(binary_string[left:right], 2)

  byte_char = str(chr(byte_int))
  #sys.stdout.write(byte_char)

print(binary_string)
count = 0
for int_value in blue:
  if count == width:
    print("")
    count = 0
  sys.stdout.write(str(chr(int_value)))
  count += 1