import urllib.request
import sys
from math import ceil
from time import sleep


matrix = [[' '] * 100 for i in range(100)]
x = 50
y = 50
matrix[y][x] = 'X'
turns_current = 0
turns_per_level = 1900 / 25
total_treasure = 0
total_attacks = 0
total_moves = 0
total_curent_kills = 0

def printMatrix(matrix):
  for i in range(100):
    for j in range(100):
      sys.stdout.write(matrix[j][i])
    print("")

def get_content(url):
  global turns_current
  turns_current += 1

  try:
    x = urllib.request.urlopen(url)
    content = str(x.read())

  except urllib.error.HTTPError as err:
    print(err)
    sleep(5)
    content = get_content(url)

  return content


def read_treasure_item(content):
  pos = content.find("<a href=\"cave.php?tres=1\">") + 26
  item = ""
  while content[pos] != '<':
    item += content[pos]
    pos += 1

  return item


def read_weapon_stats(content):
  pos = content.find("<td>Level ") + 10
  level = str(int(content[pos:pos+2]))
  pos = content.find("</td></tr>\\n<tr><td colspan=4>\\nInventory:<br>") - 1
  if content[pos].isdigit():
    plus = str(content[pos])
  else:
    plus = '0'
  return [level, plus]


def pick_up_treasure(content, url):
  global total_treasure
  if content.find("Pick up treasure:") != -1:
    item = read_treasure_item(content)
    # print("\"" + read_weapon_stats(content)[0] + "\"  " + read_weapon_stats(content)[1])
    print("Item: " + item)
    if item[-1:].isdigit():
      treasure_plus = item[-1:]
    else:
      treasure_plus = 0

    # print("\"" + str(int(item[6:8])) + "\"")
    # print(treasure_plus)
    # print(str(int(read_weapon_stats(content)[1])) + "  " + str(int(treasure_plus)))

    if item.find("potion") == -1 and (int(read_weapon_stats(content)[0]) < int(item[6:8]) or int(read_weapon_stats(content)[1]) < int(treasure_plus)):
      content = get_content(url + "&tres=1")
      print("Picked up " + item)
      total_treasure += 1

  return content



def fight_monster(content, url):
  global total_attacks, turns_current, total_curent_kills

  while content.find("Attack!") != -1:
    content = get_content(url + "&attack")
    total_attacks += 1

  if content.find("try again") != -1:
    print("Monster killed you")
    content = get_content(url + "&reset=1")
    turns_current = 0
  elif content.find("You killed the monster!") != -1:
    print("Monster died")
    content = pick_up_treasure(content, url)
    total_curent_kills += 1
  else:
    print("No monster here")

  return content


def move(url, the_move, depth):
  global matrix, x, y, init, total_moves, turns_current, turns_per_level, total_curent_kills

  total_moves += 1
  print("Move: " + the_move + " | " + str(depth))
  new_url = url
  if the_move != "":
    new_url += "&m=" + the_move
  content = get_content(new_url)
  print(content)

  content = fight_monster(content, url)

  if content.find("Dungeon Level 25") == -1:
    if content.find("Down Stairs") == -1:
      if content.find("?m=e") != -1 and matrix[y][x + 1] == ' ':
        x += 1
        matrix[y][x] = 'X'
        move(url, "e", depth + 1)
        move(url, "w", depth - 1)
      if content.find("?m=w") != -1 and matrix[y][x - 1] == ' ':
        x -= 1
        matrix[y][x] = 'X'
        move(url, "w", depth + 1)
        move(url, "e", depth - 1)
      if content.find("?m=n") != -1 and matrix[y - 1][x] == ' ':
        y -= 1
        matrix[y][x] = 'X'
        move(url, "n", depth + 1)
        move(url, "s", depth - 1)
      if content.find("?m=s") != -1 and matrix[y + 1][x] == ' ':
        y += 1
        matrix[y][x] = 'X'
        move(url, "s", depth + 1)
        move(url, "n", depth - 1)
    else:
      matrix = [[' '] * 100 for i in range(100)]
      x = 50
      y = 50
      room1 = ""
      room2 = ""
      if content.find("West") != -1:
        room1 = "&m=w"
        room2 = "&m=e"
      elif content.find("East") != -1:
        room1 = "&m=e"
        room2 = "&m=w"
      elif content.find("North") != -1:
        room1 = "&m=n"
        room2 = "&m=s"
      elif content.find("South") != -1:
        room1 = "&m=s"
        room2 = "&m=n"

      turns_current_left = turns_per_level - turns_current
      #if turns_current_left > 20:
      turns_current_left /= 6
      print(str(turns_current_left))
      while total_curent_kills < ceil(turns_current_left):
        print(total_curent_kills)
        content = get_content(url + room1)
        content = fight_monster(content, url)
        content = get_content(url + room2)
        content = fight_monster(content, url)

      turns_current = 0
      total_curent_kills = 0
      move(url, "d", 0)



name = "andreivoda"
password = "JustasimplepasswordVinti"
url = "http://www.hacker.org/challenge/misc/d/cave.php?name=" + name + "&password=" + password

try:
  move(url, "", 0)

finally:
  print("Total number of items picked up: " + str(total_treasure))
  print("Total number of beast attacks: " + str(total_attacks))
  print("Total number of moves: " + str(total_moves))