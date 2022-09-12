def palindrome(word):
  word = word.replace(' ', '').lower()
  if word[::-1] == word:
    return True
  else:
    return False


def run():
  word = input('Enter a word: ')
  if palindrome(word) == True:
    print('It is palindrome')
  else:
    print('It is not palindrome')

if __name__ == '__main__':
  run()