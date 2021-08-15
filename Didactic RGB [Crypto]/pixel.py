from PIL import Image

def main():
    im = Image.open('didactrgb.png')
    r, g, b = im.getpixel((0, 0))

    print(r * 256 ** 2 + g * 256 + b)

if __name__ == '__main__':
    main()
