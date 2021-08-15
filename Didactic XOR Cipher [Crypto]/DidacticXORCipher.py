def decrypt_xor_cipher(cipher, b, x):
    text = ''
    for byte in bytes.fromhex(cipher):
        text += chr(byte ^ b)
        b = (b + x) % 256
    return text

def main():
    encoded_bytes = '3d2e212b20226f3c2a2a2b'
    encryption_key = 79
    print(decrypt_xor_cipher(encoded_bytes, encryption_key, 0))

if __name__ == '__main__':
    main()
