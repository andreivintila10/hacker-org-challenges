import copy
import math


def multiply_with_one_digit(this_list, digit):
    number = [*this_list]

    carry = 0
    for index, num_digit in reversed(list(enumerate(number))):
      digit_mult = num_digit * digit + carry
      number[index] = digit_mult % 10
      carry = int(digit_mult / 10)

    if carry > 0:
      number.insert(0, carry)

    while len(number) > 1 and number[0] == 0:
      del number[0]

    return number


class BigNumber:
  def __init__(self, number):
    if type(number) == type([]):
      if len(number) > 0 and number[0] == '-':
        self.number = number[1:]
        self.negative = True
      else:
        self.number = number
        self.negative = False
    elif type(number) == type("") or type(number) == type(0):
      number = str(number)
      if len(number) > 0 and number[0] == '-':
        self.negative = True
        number = number[1:]
      else:
        self.negative = False

      self.number = list(map(int, number))

  def __str__(self):
    string = ""
    if self.negative:
      string = '-'
    string += ''.join(str(e) for e in self.number)

    return string

  def toString(self):
    string = ""
    if self.negative:
      string = '-'
    string += ''.join(str(e) for e in self.number)

    return string

  def convertToDecimal(self):
    dec_num = 0
    for digit in self.number:
      dec_num = dec_num * 10 + digit
    return dec_num

  def append(self, digit):
    self.number.append(digit)

  def prepend(self, digit):
    self.number.insert(0, digit)

  def remove(self, index):
    del self.number[index]

  def setNumber(self, number):
    self.number = number

  def equals(self, number):
    if len(self.number) == len(number.number):
      for index, num in enumerate(self.number):
        if num != number.number[index]:
          return False

      return True

    return False

  def isNegative(self):
    return self.negative

  def select(self, left, right):
    return BigNumber(self.number[left:right])

  def negate(self):
    if self.isNegative():
      return BigNumber(self.number)
    return BigNumber(['-'] + self.number)

  def abs(self):
    return BigNumber(self.number)

  def length(self):
    return len(self.number)

  def setDigitAt(self, index, digit):
    self.number[index] = digit

  def getDigitAt(self, index):
    return self.number[index]

  def plus(self, number):
    if not self.negative and not number.negative:
      diff = len(self.number) - len(number.number)
      if diff < 0:
        number1 = [*self.number]
        number2 = number.number
      else:
        number1 = [*number.number]
        number2 = self.number

      for index in range(abs(diff)):
        number1.insert(0, 0)

      carry = 0
      for index, digit in reversed(list(enumerate(number1))):
        digit_sum = digit + number2[index] + carry
        number1[index] = digit_sum % 10
        carry = int(digit_sum / 10)

      if carry > 0:
        number1.insert(0, carry)
      result = BigNumber(number1)
    elif self.negative and number.negative:
      result = self.abs().plus(number.abs()).negate()
    elif self.negative:
      result = number.minus(self.abs())
    elif number.negative:
      result = self.minus(number.abs())

    return result

  def multiply(self, number):
    if not self.negative and not number.negative:
      number1 = self.number
      number2 = number.number
      diff = len(number1) - len(number2)
      if diff < 0:
        temp = number1
        number1 = number2
        number2 = temp

      result = BigNumber(0)
      append0 = len(number2) - 1
      for digit in number2:
        newNumber = multiply_with_one_digit(number1, digit)
        for zeros in range(append0):
          newNumber.append(0)
        append0 -= 1
        result = result.plus(BigNumber(newNumber))
    elif self.negative and number.negative:
      result = self.abs().multiply(number.abs())
    elif self.negative:
      result = self.abs().multiply(number).negate()
    elif number.negative:
      result = self.multiply(number.abs()).negate()
    return result

  def minus(self, number):
    #print(self.toString() + " " + number.toString())
    if not self.negative and not number.negative:
      number1 = [*self.number]
      number2 = [*number.number]
      diff = len(number1) - len(number2)
      #print(str(number1.length()) + "  " + str(number2.length()))
      ok = 1
      if diff < 0:
        ok = 0
      elif diff == 0:
        for index, digit in enumerate(number1):
          compare = digit - number2[index]
          if compare < 0:
            ok = 0
            break
          elif compare > 0:
            break

      if ok == 0:
        #print("SWAPPED")
        temp = number1
        number1 = number2
        number2 = temp

      for zeros in range(abs(diff)):
        number2.insert(0, 0)

      carry = 0
      for index, digit in reversed(list(enumerate(number1))):
        diff_digit = digit - number2[index] - carry
        #print("Diff: " + str(diff_digit))
        if diff_digit < 0:
          diff_digit = 10 + diff_digit
          carry = 1
        else:
          carry = 0
        #print(str(number1.getDigitAt(index)) + "  " + str(number2.getDigitAt(index)) + "  " + str(diff_digit) + "  " + str(carry))
        number1[index] = diff_digit

      while len(number1) > 1 and number1[0] == 0:
        del number1[0]

      if ok == 0:
        number1.insert(0, '-')
      result = BigNumber(number1)
    elif self.negative and number.negative:
      result = number.abs().minus(self.abs())
    elif self.negative:
      result = self.abs().plus(number.abs()).negate()
    elif number.negative:
      result = self.plus(number.abs())

    return result

  def mod(self, number):
    if not self.negative and not number.negative:
      division = self.divide(number)
      result = self.minus(number.multiply(division))
    elif self.negative and number.negative:
      result = self.abs().mod(number.abs()).negate()
    elif self.negative:
      result = number.minus(self.abs().mod(number))
    elif number.negative:
      result = number.abs().minus(self.mod(number.abs())).negate()

    return result

  def divide(self, number):
    number1 = [*self.number]
    number2 = copy.deepcopy(number)
    number1_length = len(number1)
    number2_length = len(number2.number)
    diff = number1_length - number2_length
    if diff >= 0:
      digits_to_copy = number2_length
      newNumber = BigNumber([])
      result = []
      while number1_length > 0:
        for index in range(digits_to_copy):
          newNumber.append(number1[0])
          del number1[0]
        #print(newNumber)
        number1_length -= digits_to_copy
        count = -1
        temp = copy.deepcopy(newNumber)
        while not temp.negative:
          temp = temp.minus(number2)
          count += 1

        #print("Count: " + str(count))
        result.append(count)
        newNumber = newNumber.minus(BigNumber(multiply_with_one_digit(number2.number, count)))
        digits_to_copy = 1

      while len(result) > 1 and result[0] == 0:
        del result[0]

      return BigNumber(result)

    return BigNumber(0)