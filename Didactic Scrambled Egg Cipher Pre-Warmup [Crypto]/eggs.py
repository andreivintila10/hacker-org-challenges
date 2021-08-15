import sys
import threading


class myThread(threading.Thread):
  def __init__(self, threadID, name, range1, range2, file):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.range1 = range1
    self.range2 = range2
    self.file = file
  def run(self):
    print("Starting " + self.name)
    start_decryption(self.range1, self.range2, self.file)
    print("Exiting " + self.name)


def encrypt(eggs, key, width, loops, roll):
  for _ in range(loops):
    eggs ^= (key[eggs & 0x3] << 8)
    eggs  = (eggs << roll) | (eggs >> (width - roll))
    eggs &= ((1 << width) - 1)

  sys.stdout.write(decimal_to_hex(eggs))


def decrypt(eggs, key, width, loops, roll):
  for _ in range(loops):
    eggs = (eggs >> roll) | (eggs << (width - roll))
    eggs &= ((1 << width) - 1)
    # sys.stdout.write(str(eggs & 0x3) + " ")
    eggs ^= (key[eggs & 0x3] << 8)

  return decimal_to_plaintext(eggs)


def plaintext_to_decimal(plaintext):
  big_bytes = 0
  for char in plaintext:
    big_bytes = (big_bytes << 8) + ord(char)

  return big_bytes

def plaintext_to_decimal_little_endian(plaintext):
  decimal = ord(plaintext[0]) + (ord(plaintext[1]) << 8) + (ord(plaintext[2]) << 16)
  return decimal

def decimal_to_plaintext(decimal):
  string = ""
  for index in range(1, 4):
    value = (decimal >> (24 - index * 8)) & ((1 << 8) - 1)
    if value >= 32 and value <= 126:
      string += str(chr(value))
    else:
      return ""

  return string


def decimal_to_hex(decimal):
  return format(decimal, 'x')


def hex_to_decimal_little_endian(hex_str):
  decimal = int(hex_str[0:2], 16) + (int(hex_str[2:4], 16) << 8) + (int(hex_str[4:6], 16) << 16)
  return decimal

def find_right_xor(eggs, xor, width, loops, roll):
  mask = (255 << 16) + 255
  for index in range(loops):
    eggs = (eggs >> roll) | (eggs << (width - roll))
    eggs &= ((1 << width) - 1)
    # sys.stdout.write(str(eggs & 0x3) + " ")
    eggs = (eggs & mask) | (xor[index] << 8)

  return decimal_to_plaintext(eggs)

def start_decryption(range1, range2, f):
  text = "382d817119a18844865d880255a8221d90601ad164e8a8e1dd8a48f45846152255f839e09ab176154244faa95513d16e5e314078a97fdb8bb6da8d5615225695225674a4001a9177fb112277c45e17f85753c504d7187ed3cd43b107803827e09502559bf164292affe8aaa8e88ac898f9447119a188448692070056a2628864e6d7105edc5866b9b9b6ebcad6dc3982952a7674a62015025695225674a400d8715efb112277c45edb799f9728355c586f95b002e8aa815b83df3704571b99b6346426bd9862920721751857cb38f69bb3dee18ce1793bc857e27f74a400dd8a48d971bc15d07f521921b80948a86a8eb70457d1138279a796b8fbc43d9801e8ead669c8dcb10781788b5fe91097bad104d9ab952190a15ae706b50477b8dbe4d3cd437119c12842a42190e1a868aeb76446588d52b1078057e27cf7c65fa84aae5b8bbf6b88c19b9176a94a8eb7045778513712f1679b655d9c0255e88ac889b882b8f104711ba1dbabd7120520e188e195225655a802c184a0282affa86a8eb70457120542f7187658515f154244548a4212074278e7c6d3cd4595283e3d9a61d8ad56ba294878c5e69502551bf162487886280aff7b3309"
  key = [0] * 4
  SCR_WIDTH = 24
  SCR_LOOPS = 3
  roll = 7

  for b1 in range(range1, range2):
    key[0] = b1
    for b2 in range(256):
      key[1] = b2
      for b3 in range(256):
        key[2] = b3
        for b4 in range(256):
          key[3] = b4
          string = ""
          ok = 1
          for index in range(0, len(text), 6):
            # print(text[index - 5: index + 1])
            sub_string = decrypt(int(text[index:index + 6], 16), key, SCR_WIDTH, SCR_LOOPS, roll)
            if sub_string != "":
              string += sub_string
            else:
              ok = 0
              break

          if ok == 1:
            print(string)
            f.write(string + '\n')

  # count = 0
  # for index in range(0, len(text), 6):
  #   if count == 10:
  #     print(text[index:index + 6])
  #     decrypt(int(text[index:index + 6], 16), key, SCR_WIDTH, SCR_LOOPS, roll)
  #   count += 1


def main():
  text = "382d817119a18844865d880255a8221d90601ad164e8a8e1dd8a48f45846152255f839e09ab176154244faa95513d16e5e314078a97fdb8bb6da8d5615225695225674a4001a9177fb112277c45e17f85753c504d7187ed3cd43b107803827e09502559bf164292affe8aaa8e88ac898f9447119a188448692070056a2628864e6d7105edc5866b9b9b6ebcad6dc3982952a7674a62015025695225674a400d8715efb112277c45edb799f9728355c586f95b002e8aa815b83df3704571b99b6346426bd9862920721751857cb38f69bb3dee18ce1793bc857e27f74a400dd8a48d971bc15d07f521921b80948a86a8eb70457d1138279a796b8fbc43d9801e8ead669c8dcb10781788b5fe91097bad104d9ab952190a15ae706b50477b8dbe4d3cd437119c12842a42190e1a868aeb76446588d52b1078057e27cf7c65fa84aae5b8bbf6b88c19b9176a94a8eb7045778513712f1679b655d9c0255e88ac889b882b8f104711ba1dbabd7120520e188e195225655a802c184a0282affa86a8eb70457120542f7187658515f154244548a4212074278e7c6d3cd4595283e3d9a61d8ad56ba294878c5e69502551bf162487886280aff7b3309"
  key = [0] * 4
  SCR_WIDTH = 24
  SCR_LOOPS = 3
  roll = 7

  try:
    f = open("decoded.txt", "w")
    thread1 = myThread(1, "Thread-1", 0, 32, f)
    thread2 = myThread(2, "Thread-2", 32, 64, f)
    thread3 = myThread(3, "Thread-3", 64, 96, f)
    thread4 = myThread(4, "Thread-4", 96, 128, f)
    thread5 = myThread(5, "Thread-5", 128, 160, f)
    thread6 = myThread(6, "Thread-6", 160, 192, f)
    thread7 = myThread(7, "Thread-7", 192, 224, f)
    thread8 = myThread(8, "Thread-8", 224, 256, f)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    print("Exiting Main Thread")

  finally:
    f.close()
  # dec = plaintext_to_decimal("The")
  # print(dec)
  # print(decimal_to_plaintext(dec))
  # plaintext = "This is a secret message"
  # ciphertext = "e30f49a6e649a6e648ec8c2824ec08660649a5aceae52ea8"
  # print(str(len(ciphertext) / 2 / 3))
  # plaintext_hex = []
  # for char in plaintext:
  #   plaintext_hex.append(hex(ord(char)))
  # key = [0x11, 0x12, 0x13, 0x14]
  # for index in range(0, len(plaintext), 3):
  #   encrypt(plaintext_to_decimal(plaintext[index:index + 3]), key, SCR_WIDTH, SCR_LOOPS, roll)

  # print()
  # for index in range(0, len(ciphertext), 6):
  #   # print(text[index - 5: index + 1])
  #   sub_string = decrypt(int(ciphertext[index:index + 6], 16), key, SCR_WIDTH, SCR_LOOPS, roll)
  #   sys.stdout.write(sub_string)

  # try:
  #   union = []
  #   f = open("decoded.txt", "w")
  #   for b1 in range(32):
  #     key[0] = b1
  #     for b2 in range(126):
  #       key[1] = b2
  #       for b3 in range(126):
  #         key[2] = b3
  #         # print(str(key[0]) + " " + str(key[1]) + " " + str(key[2]))
  #         substr = find_right_xor(int(text[0:6], 16), key, SCR_WIDTH, SCR_LOOPS, roll)
  #         if substr != "":
  #           union.append([b1, b2, b3])

  #         # if ok == 1:
  #         #   print(string + "  " + str(key[0]) + " " + str(key[1]) + " " + str(key[2]))
  #         #   f.write(string + "  " + str(key[0]) + " " + str(key[1]) + " " + str(key[2]) + '\n')

  #   length = len(union)
  #   for index in range(6, len(text), 6):
  #     index2 = 0
  #     while index2 < length:
  #       substr = find_right_xor(int(text[index:index + 6], 16), union[index2], SCR_WIDTH, SCR_LOOPS, roll)
  #       if substr == "":
  #         del union[index2]
  #         length -= 1
  #       else:
  #         index2 += 1

  #   for curr_tuple in union:
  #     print(curr_tuple)
  #     string = ""
  #     for index in range(0, len(text), 6):
  #       # print(text[index - 5: index + 1])
  #       string += decrypt(int(text[index:index + 6], 16), key, SCR_WIDTH, SCR_LOOPS, roll)
  #       print(string)
  #       f.write(string + '\n')


  # try:
  #   f = open("decoded.txt", "w")
  #   for b1 in range(256):
  #     key[0] = b1
  #     for b2 in range(256):
  #       key[1] = b2
  #       for b3 in range(256):
  #         key[2] = b3
  #         for b4 in range(256):
  #           key[3] = b4
  #           string = ""
  #           ok = 1
  #           for index in range(0, len(text), 6):
  #             # print(text[index - 5: index + 1])
  #             sub_string = decrypt(int(text[index:index + 6], 16), key, SCR_WIDTH, SCR_LOOPS, roll)
  #             if sub_string != "":
  #               string += sub_string
  #             else:
  #               ok = 0
  #               break

  #           if ok == 1:
  #             print(string)
  #             f.write(string + '\n')

  # # count = 0
  # # for index in range(0, len(text), 6):
  # #   if count == 10:
  # #     print(text[index:index + 6])
  # #     decrypt(int(text[index:index + 6], 16), key, SCR_WIDTH, SCR_LOOPS, roll)
  # #   count += 1

  # finally:
  #   f.close()


main()