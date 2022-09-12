def print_message():
  print('My first function on python')

def converter_money(type_money, dollar_value):
  money = float(input('How much '+ type_money +' do you have? '))

  dollar_money = round(money / dollar_value, 2)
  dollar_money = str(dollar_money)

  print(f"You have ${dollar_money} {type_money}")

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

if options == '1':
  converter_money('pesos colombianos', 3875)
elif options == '2':
  converter_money('pesos argentinos', 65)
elif options == '3':
  converter_money('pesos mexicanos', 24)
elif options == '4':
  converter_money('soles peruanos', 3.30)
else:
  print('Enter a correct option!')
