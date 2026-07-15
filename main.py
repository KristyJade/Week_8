# week_8/main.py

import customer  
import receipt 

def main():
    print("Getting the customer data...")
    name, food, quantity, price, delivery_charges = customer.get_customer()
    
    receipt.print_receipt(name, food, quantity, price, delivery_charges)

if __name__ == "__main__":
    main()