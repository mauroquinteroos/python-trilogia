def break_keyword():
  for counter in range(100):
    if counter == 66:
      break
    print(counter)

def continue_keyword():
  for counter in range(100):
    if(counter % 2 != 0):
      continue
    print(counter)

def run():
  break_keyword()
  continue_keyword()

if __name__ == '__main__':
  run()