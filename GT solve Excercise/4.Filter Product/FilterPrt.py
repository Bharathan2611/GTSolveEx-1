"""
    4.	To the above problem statement 
    create a function to filter products that are in stock and out of stock.

    Step 1: Create a function
    Step 2: Check Inv data is dict or not then raise ValueError
    Step 3: Create two empty list for in stock and out of stock
"""
#Step 1: Create a function
def fil_stock(inv):
    #step 2: Check Inv data is dict or not then raise ValueError
    if type(inv) != dict:
        raise ValueError("Invalid inventory data")
    
    #Step 3: Create two empty list for in stock and out of stock
    in_stock = []
    out_of_stock = []
    for item, qty in inv.items():
        if qty > 0:
            in_stock.append(item)
        else:
            out_of_stock.append(item)
    return in_stock, out_of_stock

Inventory={
  "Laptop": 5,
  "Mouse": 1,
  "Keyboard": 10
}

print(fil_stock(Inventory))