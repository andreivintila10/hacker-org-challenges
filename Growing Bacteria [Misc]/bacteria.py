class Bacteria:
  def __init__(self, birthDay):
    self.birthDay = birthDay

  def lifecycle_day(self, presentDay):
    day = presentDay - self.birthDay + 1
    return day


def main():
  bacteria_alive = 1
  day = 2
  fibonacci = [0, 1]
  while bacteria_alive < 1000000000000:
    fibonacci.append(fibonacci[day - 1] + fibonacci[day - 2])
    bacteria_alive += fibonacci[day]
    if day >= 5:
      bacteria_alive -= fibonacci[day - 4]
    print("Day " + str(day) + "  T: " + str(bacteria_alive))
    day += 1


def main1():
  number_of_days = 8
  number_of_bacteria_alive = 0
  day = 1;
  bacteria = Bacteria(1)
  bacteria_population = []
  bacteria_population.append(bacteria)
  print("Day 0  B: 0  D: 0  A: 0")
  while number_of_bacteria_alive < 1000000000000:
    number_of_deaths = number_of_births = 0
    bac = 0
    population_no = len(bacteria_population)
    while bac < population_no:
      age = bacteria_population[bac].lifecycle_day(day)
      if age == 2 or age == 3:
        bacteria_population.append(Bacteria(day))
        number_of_births += 1
        bac += 1
      elif age == 5:
        del bacteria_population[bac]
        number_of_deaths += 1
      else:
        bac += 1

    number_of_bacteria_alive = len(bacteria_population)
    print("Day " + str(day) + "  B: " + str(number_of_births) + "  D: " + str(number_of_deaths) + "  A: " + str(number_of_bacteria_alive))
    number_of_deaths = number_of_births = 0
    day += 1


main()
#main1()