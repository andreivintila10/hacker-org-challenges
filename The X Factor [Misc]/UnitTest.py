from BigNumber import BigNumber


class UnitTest:
  def __init__(self, name):
    self.name = name
    self.tests_initiated = 0
    self.tests_failed = 0
    self.tests_passed = 0

  def assertTrue(self, bool):
    self.tests_initiated += 1
    if bool == True:
      self.tests_passed += 1
      return True

    self.tests_failed += 1
    return False

  def assertFalse(self, bool):
    self.tests_initiated += 1
    if bool == False:
      self.tests_passed += 1
      return True

    self.tests_failed += 1
    return False
    
  def assertArrayEquals(array1, array2):
    self.tests_initiated += 1
    array1_length = len(array1)
    if type(array1) == type([]) and type(arrray1) == type(array2) and array1_length == len(array2):
      for index in range(array1_length):
        if type(array1[index]) != type(array2[index]) or array1[index] != array2[index]:
          self.tests_failed += 1
          return False

      self.tests_passed += 1
      return True

    self.tests_failed += 1
    return False


def main():
  zero = BigNumber("0")
  one = BigNumber("1")
  seven = BigNumber("7")
  negative = BigNumber("-1")
  number1 = BigNumber("428")
  number2 = BigNumber("11111")
  number3 = BigNumber("-3124")

  t1 = UnitTest("Testing BigNumber")
  print(t1.name)
  print(t1.assertTrue(zero.multiply(number1).equals(zero)))
  print(t1.assertTrue(zero.plus(negative).equals(negative)))
  print(t1.assertTrue(number2.minus(zero).equals(number2)))
  print(t1.assertTrue(number2.divide(number1).equals(BigNumber("25"))))
  print(t1.assertTrue(number2.mod(number1).equals(BigNumber("411"))))
  print(str(t1.tests_passed) + "/" + str(t1.tests_initiated))

  print(BigNumber(13841287201).divide(seven))

  count = 0
  bg_number = BigNumber("167")
  bg_number2 = BigNumber("28679718602997181072337614380936720482949")
  temp = one
  while not bg_number.minus(seven).isNegative() and not bg_number.minus(seven).equals(zero):
    bg_number = bg_number.divide(seven)
    temp = temp.multiply(seven)
    count += 1

  temp = temp.divide(seven)
  print(temp)
  print(bg_number.toString() + " " + str(count))


main()