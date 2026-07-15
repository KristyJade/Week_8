# week_8/receipt.py

def print_receipt(name, food, quantity, price, delivery_charge):
    
    subtotal = quantity * price
    
    service_charge = subtotal * 0.05
    
    grand_total = subtotal + service_charge + delivery_charge
    
    print("\n========== RECEIPT ==========")
    
    print(f"Customer : {name}")
    print(f"Food     : {food}")
    print(f"Quantity : {quantity}")
    print(f"Price    : RM {price:.2f}")
    
    print("-----------------------------")
    
    print(f"{'Subtotal':<19} : RM {subtotal:.2f}")
    print(f"{'Service Charge (5%)':<19} : RM {service_charge:.2f}")
    print(f"{'Delivery Charge':<19} : RM {delivery_charge:.2f}")
    
    print("-----------------------------")
    print(f"Grand Total : RM {grand_total:.2f}")
    print("=============================")