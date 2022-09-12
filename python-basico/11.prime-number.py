def validate_prime(number):
  prime = 0
  for i in range(1, number + 1):
    if number % i == 0:
      prime += 1
  if prime == 2:
    return True
  else:
    return False


def run():
  for i in range(1,101):
    if(validate_prime(i)):
      print(i)


if __name__ == '__main__':
  run()