def init_key_map():
  keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
  values = ["is", "mm", "oo", "rgr", "ryg", "dth", "you", "esol", "ionA", "GDaBarA", "veECFHutI", "PQ", "n", "m", "oaNcho", "MO", "NR", "sky", "JKL"]
  return dict(zip(keys, values))


def expand(key_map, key):
  string = ""
  for letter in key_map[key]:
    if letter in key_map.keys():
      string += expand(key_map, letter)
    else:
      string += letter

  return string


def main():
  key_map = init_key_map()
  print(expand(key_map, 'S'))


main()