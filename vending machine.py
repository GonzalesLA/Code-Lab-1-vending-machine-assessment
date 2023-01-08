#A menu of drinks & snacks.
items_in_stock = [
      {
          'item_id': 10,
          'item_name': 'soda ',
          'item_price': 2.75,
      },
      {
          'item_id': 11,
          'item_name': 'water',
          'item_price': 1.00,
      },
      {
          'item_id': 12,
          'item_name': 'chips',
          'item_price': 2.50,
      },
      {
          'item_id': 13,
          'item_name': 'candy',
          'item_price': 3.00,
      },
      {
          'item_id': 14,
          'item_name': 'iced tea',
          'item_price': 3.75,
      },

  ]

  #To show what's available in the vending machine.
print("Hello! Welcome to my vending machine!")
print("These are the items available in this vending machine, please select an item\n")

for i in items_in_stock:
  print(f"item: {i['item_name']} | Price: {i['item_price']} | Code: {i['item_id']}")

def calculate():
  while True:
#To show what's available in the vending machine.

    #Program when the user chose an item ID.
    selected_item = int(input("\nPlease input your item's code: "))
    if selected_item == 10:
      print("\nYou have selected \"soda\". That will cost 2.75.")
      cash = float(input("\nPlease enter your the amount of cash you have: "))
      if cash == 2.75:
        print('\nYour transaction has been successful. \nThank you for using my vending machine. Enjoy your snack.')
      if cash > 2.75:
        print(f"\nYour change is: {(cash - 2.75)} \nThank you for using my vending machine. Enjoy your snack.")
      if cash < 2.75:
          print("\nNot enough amount equivalent to the item, please start over again")
      break

    elif selected_item == 11:
        print("\nYou have selected \"water\". That will cost 1.00.")
        cash = float(input("\nPlease enter your the amount of cash you have: "))
        if cash == 1.00:
          print('\nYour transaction has been successful. \nThank you for using my vending machine. Enjoy your snack.')
        if cash > 1.00:
          print(f"\nYour change is: {(cash - 1)} \nThank you for using my vending machine. Enjoy your snack.")
        if cash < 2.75:
          print("Not enough amount equivalent to the item, please start over again")
        break

    elif selected_item == 12:
        print("\nYou have selected \"chips\". That will cost 2.50.")
        cash = float(input("\nPlease enter your the amount of cash you have: "))
        if cash == 2.50:
          print('\nYour transaction has been successful. \nThank you for using my vending machine. Enjoy your snack.')
        if cash > 2.50:
          print(f"\nYour change is: {(cash - 2.50)} \nThank you for using my vending machine. Enjoy your snack.")
        if cash < 2.50:
          print("Not enough amount equivalent to the item, please start over again")
        break
        
    elif selected_item == 13:
        print("\nYou have selected \"candy\". That will cost 3.00.")
        cash = float(input("\nPlease enter your the amount of cash you have: "))
        if cash == 3.00:
          print('\nYour transaction has been successful. \nThank you for using my vending machine. Enjoy your snack.')
        if cash > 3.00:
          print(f"\nYour change is: {(cash - 3)} \nThank you for using my vending machine. Enjoy your snack.")
        if cash < 2.75:
          print("Not enough amount equivalent to the item, please start over again")
        break

    elif selected_item == 14:
        print("\nYou have selected \"iced tea\". That will cost 3.75.")
        cash = float(input("\nPlease enter your the amount of cash you have: "))
        if cash == 3.75:
          print('\nYour transaction has been successful. \nThank you for using my vending machine. Enjoy your snack.')
        if cash > 3.75:
          print(f"\nYour change is: {(cash - 3.75)} \nThank you for using my vending machine. Enjoy your snack")
        if cash < 2.75:
          print("Not enough amount equivalent to the item, please start over again")
        break

calculate()