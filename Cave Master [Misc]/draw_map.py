import sys
import urllib.request


matrix = [[' '] * 30 for i in range(30)]
x = 15
y = 15


def read_treasure_item(content):
  pos = content.find("<a href=\"cave.php?tres=1\">") + 26
  item = ""
  while content[pos] != '<':
    item += content[pos]
    pos += 1

  return item


def printMatrix(matrix):
  for i in range(30):
    for j in range(30):
      sys.stdout.write(matrix[j][i])
    print("")


def get_content(url):
  x = urllib.request.urlopen(url)
  return str(x.read())


def pick_up_treasure(content, url):
  if content.find("Pick up treasure:") != -1:
    item = read_treasure_item(content)
    print("Item: " + item)
    if item.find("potion") == -1:
      content = get_content(url + "&tres=1")
      print("Picked up " + item)

  return content


def fight_monster(content, url):
  while content.find("Attack!") != -1:
    content = get_content(url + "&attack")

  if content.find("try again") != -1:
    print("Monster killed you")
  elif content.find("You killed the monster!") != -1:
    print("Monster died")
    content = pick_up_treasure(content, url)
  else:
    print("No monster here")

  return content


def move(url, the_move, depth):
  global matrix, x, y

  print("Move: " + the_move + " | " + str(depth))
  new_url = url
  if the_move != "":
    new_url += "&m=" + the_move
  content = get_content(new_url)
  #print(content)
  #printMatrix(matrix)

  content = fight_monster(content, url)

  if content.find("?m=e") != -1 and matrix[y][x + 1] == ' ':
    x += 1
    matrix[y][x] = 'X'
    move(url, "e", depth + 1)
    move(url, "w", depth)
  if content.find("?m=w") != -1 and matrix[y][x - 1] == ' ':
    x -= 1
    matrix[y][x] = 'X'
    move(url, "w", depth + 1)
    move(url, "e", depth)
  if content.find("?m=n") != -1 and matrix[y - 1][x] == ' ':
    y -= 1
    matrix[y][x] = 'X'
    move(url, "n", depth + 1)
    move(url, "s", depth)
  if content.find("?m=s") != -1 and matrix[y + 1][x] == ' ':
    y += 1
    matrix[y][x] = 'X'
    move(url, "s", depth + 1)
    move(url, "n", depth)


name = "andreivoda"
password = "JustasimplepasswordVinti"
url = "http://www.hacker.org/challenge/misc/d/cave.php?name=" + name + "&password=" + password

move(url, "", 0)
#printMatrix(matrix)