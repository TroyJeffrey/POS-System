# Import POS to access class and checkout function

import POS

print("++++++WELCOME TO THE COASTAL BAKERY++++++\n")
Menu = 0

# While loop to allow user access to menu until checkout

while Menu != 11:
    print('Select an Item from the menu below to add to your cart. Press 11 to Check Out\n')
    print('1. Chocolate Chip Cookie ')
    print('2. Blueberry Muffin')
    print('3. Glazed Donut')
    print('4. Birthday Cake')
    print('5. Red Velvet Cake')
    print('6. Cinnamon Roll')
    print('7. Plain Bagel')
    print('8. Blueberry Bagel')
    print('9: Cinnamon Bagel')
    print('10. Iced Coffee')
    print('11. CHECK OUT')

# Customer inputs number to add item to cart

    Menu = int(input('\n>'))

# if statements add item to cart if customer chooses associated number

    if Menu == 1:
        POS.ChocolateChipCookie.add_to_cart()

    elif Menu == 2:
        POS.BlueberryMuffin.add_to_cart()

    elif Menu == 3:
        POS.GlazedDonut.add_to_cart()

    elif Menu == 4:
        POS.BirthdayCake.add_to_cart()

    elif Menu == 5:
        POS.RedVelvetCake.add_to_cart()

    elif Menu == 6:
        POS.CinnamonRoll.add_to_cart()

    elif Menu == 7:
        POS.PlainBagel.add_to_cart()

    elif Menu == 8:
        POS.BlueberryBagel.add_to_cart()

    elif Menu == 9:
        POS.CinnamonBagel.add_to_cart()

    elif Menu == 10:
        POS.IcedCoffee.add_to_cart()

# When customer is ready to check out, they hit 11

    elif Menu == 11:
        # Checkout function from POS python file is called to complete checkout
        POS.check_out()


