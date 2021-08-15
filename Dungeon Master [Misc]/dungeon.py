import urllib.request
import sys


matrix = [[' '] * 100 for i in range(100)]
x = 50
y = 50
matrix[y][x] = 'X'

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


def fight_monster(content, url):
  while content.find("Attack!") != -1:
    content = get_content(url + "&attack")

  if content.find("try again") != -1:
    print("Monster killed you")
  else:
    print("Monster died")
    pick_up_treasure(content, url)

  return content


def move(url, the_move):
  global matrix, x, y
  print("Move: " + the_move)
  new_url = url
  if the_move != "":
    new_url += "&m=" + the_move
  content = get_content(new_url)
  print(content)

  content = fight_monster(content, url)

  if content.find("Down Stairs") == -1:
    if content.find("?m=e") != -1 and matrix[y][x + 1] == ' ':
    	x += 1
    	matrix[y][x] = 'X'
    	move(url, "e")
    if content.find("?m=w") != -1 and matrix[y][x - 1] == ' ':
    	x -= 1
    	matrix[y][x] = 'X'
    	move(url, "w")
    if content.find("?m=n") != -1 and matrix[y - 1][x] == ' ':
    	y -= 1
    	matrix[y][x] = 'X'
    	move(url, "n")
    if content.find("?m=s") != -1 and matrix[y + 1][x] == ' ':
    	y += 1
    	matrix[y][x] = 'X'
    	move(url, "s")
  else:
    #print(content)
    matrix = [[' '] * 100 for i in range(100)]
    x = 50
    y = 50
    move(url, "d")



name = "andreivoda"
password = "JustasimplepasswordVinti"
url = "http://www.hacker.org/challenge/misc/d/index.php?name=" + name + "&password=" + password

# for index in range (50):
#   content = get_content(url + "&m=e")
#   fight_monster(content, url)
#   content = get_content(url + "&m=w")
#   fight_monster(content, url)

move(url, "")