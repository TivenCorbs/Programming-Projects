#No Exceptions, imports,
print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
print("Stock contains:")
stock = {
     "nickels": 25,
     "dimes": 25,
     "quarters":25,
     "ones" : 0,
     "fives" : 0
}
print ('\n'.join(f'   {value} {key}' for key, value in stock.items()))

acceptance_char = {'0','1','2','3','4','5','6','7','8','9','.','-'}

#for int in input

#if number is digit

#else break stop program

while (True):
  print("")
  purchaseprice = (input("Enter the purchase price (xx.xx) or `q\' to quit:"))
  if (purchaseprice == 'q'):
    break

  # Input validation
  if not set(purchaseprice).issubset(acceptance_char):
    print("Invalid purchase price. Try again")
    break

  if float(purchaseprice) * 100 % 5 != 0 or float(purchaseprice) < 0:
    print("")
    print("Illegal price: Must be a non-negative multiple of 5 cents.")
    continue

  # Payment
  purchaseprice = int(float(purchaseprice)*100)
  remaining_cost = purchaseprice
  print("")
  print("Menu for deposits:\n  'n' - deposit a nickel\n  'd' - deposit a dime\n  'q' - deposit a quarter\n  'o' - deposit a one dollar bill\n  'f' - deposit a five dollar bill\n  'c' - cancel the purchase\n")

  change_owed = 0

  while remaining_cost > 0:
    print(f'Payment due: {int(remaining_cost/100)} dollars and {(remaining_cost%100)} cents')
    choice = input('Indicate your deposit:')
    print("")
    if choice =='n':
      remaining_cost -= 5
      stock['nickels'] += 1

    elif choice =='d':
      remaining_cost -= 10
      stock["dimes"] += 1

    elif choice =='q':
      remaining_cost -= 25
      stock["quarters"] += 1

    elif choice =='o':
      remaining_cost -= 100
      stock['ones'] += 1

    elif choice =='f':
      remaining_cost -= 500
      stock["fives"] += 1

    elif choice =='c':
      change_owed = purchaseprice - remaining_cost
      break

    else:
      print('Illegal Selection:', choice)
  

  # Payment change
  if (remaining_cost < 0):
    change_owed = 0 - remaining_cost

  coin_exchange = {
    "nickels": 0,
    "dimes": 0,
    "quarters": 0,
  }

  while (change_owed > 0):
    if (change_owed >= 25 and stock['quarters'] > 0):
      #Take one out of stock
      stock['quarters'] -= 1
      #Place it in coin exchange
      coin_exchange['quarters'] +=1
      #Decrement change_owed by coin value (deducts 25 from amount owned)
      change_owed -= 25

    elif (change_owed >= 10 and stock['dimes'] > 0):
      stock['dimes'] -= 1
      coin_exchange['dimes'] +=1
      change_owed -= 10

    elif (change_owed >= 5 and stock['nickels'] > 0):
      stock['nickels'] -= 1
      coin_exchange['nickels'] += 1
      change_owed -= 5
    
    else:
      break



  print("Please take the change below.") 
  if (coin_exchange['quarters'] > 0):
    print(f"   {coin_exchange['quarters']} quarters")

  if (coin_exchange['nickels'] > 0):
    print(f"   {coin_exchange['nickels']} nickels")

  if (coin_exchange['dimes'] > 0):
    print(f"   {coin_exchange['dimes']} dimes")

  if (change_owed > 0):
    print("See manager for remaining refund")
    print(f'Amount due is: {int(change_owed//100)} dollars and {int(change_owed%100)} cents')

#No coins in the machine
  if(change_owed == 0 and coin_exchange['quarters']==0 and coin_exchange['dimes']==0 and coin_exchange['nickels']==0 ):
        print("  No change due.")

  print("")
  print("Change maker initalized")
  print("Stock contains:")
  print('\n'.join(f'   {value} {key}' for key, value in stock.items()))
  print("")

total = (stock["quarters"]*25) + (stock["dimes"]*10) + (stock['nickels']*5) + (stock['ones']*100) + (stock['fives']*500)
 
print("")
print(f"Total: {int(total//100)} dollars and {int(total%100)} cents")


