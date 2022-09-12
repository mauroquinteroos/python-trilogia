def run():
  dictionary = {
    'key1': 1,
    'key2': 2,
    'key3': 3
  }
  population = {
    'Argentina': 449_387_115,
    'Peru': 210_417_125,
    'Colombia': 315_657_982
  }

  for country in population.keys():
	  print(country)

  for country in population.values():
	  print(country)

  for country, value in population.items():
	  print(country, value)

if __name__ == '__main__':
  run()