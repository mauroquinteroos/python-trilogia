import random


def aleatory():
  aleatory_number = random.randint(1, 100)
  chosen_number = int(input('Choose a number between 1 and 100: '))
  while chosen_number != aleatory_number:
    if chosen_number > aleatory_number:
      print('Choose a new number more smaller')
    else:
      print('Chosse a number more bigger')
    chosen_number = int(input('Choose another number: '))
  print('You win!')


def run():
  aleatory()


if __name__ == '__main__':
  run()
