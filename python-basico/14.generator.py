import random

def passsword_generator():
  upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  symbols = ['!', '#', '$', '&', '/', '*', 'ˆ']

  characters = upper + lower + symbols
  password = []
  for i in range(15):
    character_random = random.choice(characters)
    password.append(character_random)
  password = ''.join(password) # Join all list items in a string
  return password


def run():
  password = passsword_generator()
  print('Your new password is: ' + password)

if __name__ == '__main__':
  run()