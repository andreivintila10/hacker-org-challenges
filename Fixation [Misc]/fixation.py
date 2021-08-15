from PIL import Image
from PIL import GifImagePlugin


def main():
  imageObject = Image.open("swirl.gif")
  print(imageObject.is_animated)
  print(imageObject.n_frames)

  # Display individual frames from the loaded animated GIF file.
  for frame in range(0, imageObject.n_frames):
    imageObject.seek(frame)
    imageObject.show()


if __name__ == '__main__':
  main()