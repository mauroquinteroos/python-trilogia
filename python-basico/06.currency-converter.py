menu = """
Welcome the currency converter
-------------------------------
1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos
4. Soles peruanos
-------------------------------
Enter your option: """

options = input(menu)

if options == 1:
  soles_money = float(input('How much pesos colombianos do you have? '))
  dollar_value = 3875
  dollar_money = round(soles_money / dollar_value, 2)
  dollar_money = str(dollar_money)
  print('You have $' + dollar_money + ' dollars')
elif options == 2:
  soles_money = float(input('How much pesos argentinos do you have? '))
  dollar_value = 65
  dollar_money = round(soles_money / dollar_value, 2)
  dollar_money = str(dollar_money)
  print('You have $' + dollar_money + ' dollars')
elif options == 3:
  soles_money = float(input('How much pesos mexicanos do you have? '))
  dollar_value = 24
  dollar_money = round(soles_money / dollar_value, 2)
  dollar_money = str(dollar_money)
  print('You have $' + dollar_money + ' dollars')

elif options == 4:
  soles_money = float(input('How much soles peruanos do you have? '))
  dollar_value = 3.30
  dollar_money = round(soles_money / dollar_value, 2)
  dollar_money = str(dollar_money)
  print('You have $' + dollar_money + ' dollars')
else:
  print('Enter a correct option!')
