def main():
  text = "mQmPtphqGrboHhmgaqVhCdwTwignlQvjIopDqVpgaNrwkAzVcnkHyNiPdSmgJmgrPiMjpnjdbuPucHnouwfKuPcybromnmbvfxJqRnnOvWsceZeYzRyqnkaaFsffjenxoIhqHnIzorlOdwZoxYmAuNwNnRppguwidvbtOqdbUngpZdbGqwYjfpLzPjRtwVwEqBbYmCqbKwuziCoEwPsIkJgruTbhdyWpvPztAodufjZxLaZcUeFaklSmeRfolohVbXoDfIqMqgIrQhzedqZlFwaBndQkQexBdLsCfXebrEfiOnSgYquyaqohxoDmLdDhwoOpgtkuRzeYziuvnuvnUuOtqasZueYpKfAkmKcJcWeocQvJguVsZfVovgrztAiryZivHqyMjoLyJdklKifmoWeOjVnogiiaBzDfrsWlOeAzPxltamqQiujZrpZrUcIlyktdJbhmNpDbltOlLnAqVhcxgObghpdcScgIiayqygUgwatiEzgzTsZgApUbbPynLfbzehzWsxcPbdcdfMucsCzjkWvjhMkiWuHfquqrcKwedqghiyHyMkSayRegeJcGw" 
  count = 0
  for index in range(len(text)):
    if text[index].islower():
      count += 1
  print("Count: " + str(count))


main()