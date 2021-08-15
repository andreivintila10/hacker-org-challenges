import sys
from PIL import Image

im = Image.open('greenline.png')
rgb_im = im.convert('RGB')
width, height = im.size
green = []
for index in range(width):
  r, g, b = rgb_im.getpixel((index, 0))
  green.append(g);

for int_value in green:
  sys.stdout.write(str(chr(int_value)))