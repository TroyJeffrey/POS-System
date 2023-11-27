# Troy Amegashie
# POS Project


class MenuItem:
    # Declare class variables
    cart = []  # Create a class list to store items in the cart
    total = 0
    tax = 0
    discount = 0
    grand_total = 0

    # Initialization of values

    def __init__(self, item_number, item_name, item_price, item_description, item_discount, item_tax,):
        self.item_number = item_number
        self.item_name = item_name
        self.item_price = item_price
        self.item_description = item_description
        self.item_discount = item_discount
        self.item_tax = item_tax

    # Class method to add to cart

    def add_to_cart(self):
        MenuItem.cart.append(self.item_name)  # Class variable 'cart' is updated
        MenuItem.total = self.item_price + self.total  # Adds item price and class variable 'total' is updated
        MenuItem.tax = self.tax + self.item_tax  # Adds item tax and class variable 'tax' is updated
        MenuItem.discount = self.discount + self.item_discount  # Adds item discount and lass variable 'discount is updated'
        print(self.item_name, 'has been added to your cart\n')


# Function created to check customer out
# The purchase option will call on this function
def check_out():
    print('Here is your cart:\n')  # Cart list is printed
    for x in MenuItem.cart:
        print(x)
    print('\nYour total is $', MenuItem.total)  # Class variable total prints final value
    print()
    print('Tax = $', MenuItem.tax)  # Class variable 'tax' prints final value
    print('Discount = $', MenuItem.discount)  # Class variable 'discount' prints final value
    s = MenuItem.tax - MenuItem.discount  # 's' variable subtracts discount from tax
    grand_total = MenuItem.total + s  # grand total is calculated by adding value of 's'
    print('Your grand total is $', grand_total)
    print()
    receive = int(input('Amount Received: '))  # User is prompted to enter the amount of cash they are paying with
    print('Change: $', receive - grand_total)  # Change is calculated by subtracting grand total from money received
    print('\n++++CUSTOMER RECEIPT++++')

    # Customer Receipt is printed
    print("Items Purchased:\n")
    for x in MenuItem.cart:
        print(x)
    print('\nTotal: $', MenuItem.total, '\nTax: $', MenuItem.tax,
          '\nDiscount: $', MenuItem.discount, '\nGrand Total: $', grand_total)

    print('\n++++THANK YOU! COME AGAIN!++++')


# Class objects are created

ChocolateChipCookie = MenuItem(1, 'Chocolate Chip Cookie', 3, 'Soft cookie with Swiss Chocolate', 0, 0.45)
BlueberryMuffin = MenuItem(2, 'Blueberry Muffin', 4, 'Freshly baked blueberry muffin', 0.5, 0.35)
GlazedDonut = MenuItem(3, 'Glazed Donut', 3, 'Old fashioned donut topped with glaze', 0, 1)
BirthdayCake = MenuItem(4, 'Birthday Cake', 6, 'A delicious slice fo birthday cake', 0, 1)
RedVelvetCake = MenuItem(5, 'Red Velvet Cake', 7, 'A delicious slice of red velvet cake', 2, 1)
CinnamonRoll = MenuItem(6, 'Cinnamon Roll', 5, 'Freshly baked cinnamon roll', 1, 2)
PlainBagel = MenuItem(7, 'Plain Bagel', 3, 'Freshly baked plain white bagel', 0, 0.3)
BlueberryBagel = MenuItem(8, 'Blueberry Bagel', 3.5, 'Freshly baked blueberry bagel', 0, 0.4)
CinnamonBagel = MenuItem(9, 'Cinnamon Bagel', 3.75, 'Freshly baked cinnamon bagel', 0, 0.2)
IcedCoffee = MenuItem(10, 'Iced Coffee', 5, 'Cold Brew', 0, 0.3)
