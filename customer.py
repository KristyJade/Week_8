# week_8/customer.py

def get_customer():

    print("=== Customer Information ===")
 
    name = input("Customer Name : ")
    food = input("Food Ordered (Cake/Muffin) : ")
    quantity = int(input("Quantity : "))
    price = float(input("Price per Item (RM): "))
    delivery = input("Delivery (Y/N): ").upper()  # .upper() handles 'y' or 'Y'

    if delivery == 'Y':
        delivery_charges = 5.00
    else:
        delivery_charges = 0.00

    return name, food, quantity, price, delivery_charges