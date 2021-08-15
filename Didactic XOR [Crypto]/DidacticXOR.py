def main():
    byte1 = '9f'
    byte2 = 'c7'
    print(chr(int(byte1, base=16) ^ int(byte2, base=16)))

if __name__ == '__main__':
    main()
