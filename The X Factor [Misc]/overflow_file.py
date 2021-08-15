f = open("test.txt", "w")
for index in range(100000000):
  f.write("999999999" + ' ')

f.close()