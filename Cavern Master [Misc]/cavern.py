import urllib.request
import sys


matrix = [[' '] * 100 for i in range(100)]
x = 50
y = 50
matrix[y][x] = 'X'
init = 1

def printMatrix(matrix):
  for i in range(100):
    for j in range(100):
      sys.stdout.write(matrix[j][i])
    print("")

def get_content(url):
  x = urllib.request.urlopen(url)
  return str(x.read())


def pick_up_treasure(content, url):
  if content.find("Pick up treasure:") != -1:
    content = get_content(url + "&tres=1")
    print("Picked up treasure")

  return content



def fight_monster(content, url):
  while content.find("Attack!") != -1:
    content = get_content(url + "&attack")

  if content.find("try again") != -1:
    print("Monster killed you")
  elif content.find("You killed the monster!") != -1:
    print("Monster died")
    #content = pick_up_treasure(content, url)
  else:
    print("No monster here")

  return content


def move(url, the_move, depth):
  global matrix, x, y, init

  print("Move: " + the_move + " | " + str(depth))
  new_url = url
  if the_move != "":
    new_url += "&m=" + the_move
  content = get_content(new_url)
  print(content)

  content = fight_monster(content, url)

  if init == 1:
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

    for index in range (10):
      print(index)
      content = get_content(url + room1)
      content = fight_monster(content, url)
      content = get_content(url + room2)
      content = fight_monster(content, url)
    init = 0

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
    #print(content)
    matrix = [[' '] * 100 for i in range(100)]
    x = 50
    y = 50
    init = 1
    move(url, "d", 0)



name = "andreivoda"
password = "JustasimplepasswordVinti"
url = "http://www.hacker.org/challenge/misc/d/cavern.php?name=" + name + "&password=" + password

room1 = "&m=w"
room2 = "&m=e"
for index in range (300):
  print(index)
  content = get_content(url + room1)
  content = fight_monster(content, url)
  content = get_content(url + room2)
  content = fight_monster(content, url)

#move(url, "", 0)