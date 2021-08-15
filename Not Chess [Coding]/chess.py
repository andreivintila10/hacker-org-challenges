def encodeIt(input_string):
  keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

  # input_string = escape(input_string)
  output = ""
  chr1 = chr2 = chr3 = ""
  enc1 = enc2 = enc3 = enc4 = ""
  i = 3

  chr1 = ord(input_string[0])
  chr2 = ord(input_string[1])
  chr3 = ord(input_string[2])

  enc1 = chr1 >> 2
  enc2 = ((chr1 & 3) << 4) | (chr2 >> 4)
  enc3 = ((chr2 & 15) << 2) | (chr3 >> 6)
  enc4 = chr3 & 63

  if not str(chr(chr2)).isdigit():
    enc3 = enc4 = 64;
  elif not str(chr(chr3)).isdigit():
    enc4 = 64;

  output += keyStr[enc1] + keyStr[enc2] + keyStr[enc3] + keyStr[enc4]
  chr1 = chr2 = chr3 = ""
  enc1 = enc2 = enc3 = enc4 = ""

  while i < len(input_string):
    chr1 = ord(input_string[i])
    i += 1
    chr2 = ord(input_string[i])
    i += 1
    chr3 = ord(input_string[i])
    i += 1

    enc1 = chr1 >> 2
    enc2 = ((chr1 & 3) << 4) | (chr2 >> 4)
    enc3 = ((chr2 & 15) << 2) | (chr3 >> 6)
    enc4 = chr3 & 63

    if not str(chr(chr2)).isdigit():
      enc3 = enc4 = 64;
    elif not str(chr(chr3)).isdigit():
      enc4 = 64;

    output += keyStr[enc1] + keyStr[enc2] + keyStr[enc3] + keyStr[enc4]
    chr1 = chr2 = chr3 = ""
    enc1 = enc2 = enc3 = enc4 = ""

  return output


def lockpick(match):
  string = [32, 32, 32]
  for ch0 in range(32, 127):
    string[0] = str(chr(ch0))

    for ch1 in range(32, 127):
      string[1] = str(chr(ch1))

      for ch2 in range(32, 127):
        string[2] = str(chr(ch2))

        if encodeIt(''.join(string)) == match:
          print(''.join(string))
          return ''.join(string)

  return "    "


def decodeIt(match):
  seq = 4
  groups = int(len(match) / seq)
  main_string = ""
  left = 0
  right = seq
  for gr in range(groups):
    gr_string = match[left:right]
    main_string += lockpick(gr_string)
    left = right;
    right += seq;

  return main_string;

print(decodeIt("cXVlZW4lMjdzJTIwZ2FtYml0"))