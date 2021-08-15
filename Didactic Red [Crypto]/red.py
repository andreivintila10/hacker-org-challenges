import sys
from PIL import Image

im = Image.open('redline.png')
rgb_im = im.convert('RGB')
red = []
for index in range(4):
  r, g, b = rgb_im.getpixel((index, 0))
  red.append(r);

for int_value in red:
  sys.stdout.write(format(int_value, '02x'))