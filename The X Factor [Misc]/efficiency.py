import time
import matplotlib.pyplot as plt


#Less efficient
def loop1(my_list, length):
  for el in range(length):
    if my_list[el] == 0:
      my_list[el] = 1

# Most efficient for accessing elements
def loop2(my_list, length):
  for el in my_list:
    continue

#Most efficient for accessing and modifying if needed
def loop3(my_list, length):
  for index, el in enumerate(my_list):
    if el == 0:
      my_list[index] = 1

#Least efficient
def loop4(my_list, length):
  index = 0
  while index < length:
    if my_list[index] == 0:
      my_list[index] = 1
    index += 1


def plot_graph_loop(x1, y1, x2, y2, x3, y3):
  plt.plot(x1, y1, label = "in range")
  plt.plot(x2, y2, label = "for each")
  plt.plot(x3, y3, label = "while")

  plt.xlabel("Elements")
  plt.ylabel("Seconds")
  plt.title("Efficiency test of for loops")

  plt.legend()
  plt.show()


def loop_test_run():
  lengths = [2, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
  x1 = x2 = x3 = [*lengths]
  y1 = []
  y2 = []
  y3 = []
  t = 0

  for length in lengths:
    my_list = [0, 1] * int(length / 2)
    time_sum = 0.0
    for index in range(3):
      t = time.time()
      loop1(my_list, length)
      delta = time.time() - t
      print("%.20f" % delta)
      time_sum += delta

      my_list = [0, 1] * int(length / 2)

    y1.append(time_sum / 3.0)
    # t = time.time()
    # loop2(my_list, length)
    # print("%.20f" % (float(time.time() - t)))

    # print(my_list[0])
    # my_list = [0, 1] * int(length / 2)
    time_sum = 0.0
    for index in range(3):
      t = time.time()
      loop3(my_list, length)
      delta = time.time() - t
      print("%.20f" % delta)
      time_sum += delta

      my_list = [0, 1] * int(length / 2)

    y2.append(time_sum / 3.0)


    time_sum = 0.0
    for index in range(3):
      t = time.time()
      loop4(my_list, length)
      delta = time.time() - t
      print("%.20f" % delta)
      time_sum += delta

    y3.append(time_sum / 3.0)

  plot_graph_loop(x1, y1, x2, y2, x3, y3)


def shorthand_increment(times):
  count = 0
  for index in range(times):
    count += 1

def normal_increment(times):
  count = 0
  for index in range(times):
    count = count + 1

def plot_graph_increment(x1, y1, x2, y2):
  plt.plot(x1, y1, label = "shorthand")
  plt.plot(x2, y2, label = "normal")

  plt.xlabel("Increments")
  plt.ylabel("Seconds")
  plt.title("Efficiency test for increment")

  plt.legend()
  plt.show()

def increment_test_run():
  lengths = [2, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
  x1 = x2 = [*lengths]
  y1 = []
  y2 = []
  t = 0

  for length in lengths:
    time_sum = 0.0
    for index in range(3):
      t = time.time()
      shorthand_increment(length)
      delta = time.time() - t
      print("%.20f" % delta)
      time_sum += delta

    y1.append(time_sum / 3.0)

    time_sum = 0.0
    for index in range(3):
      t = time.time()
      normal_increment(length)
      delta = time.time() - t
      print("%.20f" % delta)
      time_sum += delta

    y2.append(time_sum / 3.0)

  plot_graph_increment(x1, y1, x2, y2)


def append_function(length):
  my_list = []
  for index in range(length):
    my_list.append(0)

def append_with_indexing(length):
  my_list = [0] * length
  n = 0
  for index in range(length):
    my_list[n] = 1
    n += 1

def plot_graph_append(x1, y1, x2, y2):
  plt.plot(x1, y1, label = "Append")
  plt.plot(x2, y2, label = "Indexing")

  plt.xlabel("Appends")
  plt.ylabel("Seconds")
  plt.title("Efficiency test for appending")

  plt.legend()
  plt.show()

def append_test_run():
  lengths = [2, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
  x1 = x2 = [*lengths]
  y1 = []
  y2 = []
  t = 0

  for length in lengths:
    time_sum = 0.0
    for index in range(3):
      t = time.time()
      append_function(length)
      delta = time.time() - t
      print("%.20f" % delta)
      time_sum += delta

    y1.append(time_sum / 3.0)

    time_sum = 0.0
    for index in range(3):
      t = time.time()
      append_with_indexing(length)
      delta = time.time() - t
      print("%.20f" % delta)
      time_sum += delta

    y2.append(time_sum / 3.0)

  plot_graph_append(x1, y1, x2, y2)


def main():
  # loop_test_run()
  # increment_test_run()
  # append_test_run()
  test = """
  my_list = [] * 
  for i in xrange(50):
    my_list += [0]
  """
  timeit(test)


main()