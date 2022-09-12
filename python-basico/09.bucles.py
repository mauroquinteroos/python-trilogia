def while_loop():
  LIMIT = 150
  counter = 0
  potency = 2 ** counter
  while potency < LIMIT:
    print('2 elevado a '+ str(counter) +' es igual a: '+ str(potency))
    counter += 1
    potency = 2 ** counter


def for_loop():
  for counter1 in range(10):
    print(counter1+1)

  for counter2 in range(1, 11):
    print(counter2)


def loop_string():
  name = input('Write a name: ')
  for char in name:
    print(char)


def run():
  print("Run all these options")
  # 1. while_loop()
  # 2. for_loop()
  # 3. loop_string()

if __name__ == '__main__':
  run()