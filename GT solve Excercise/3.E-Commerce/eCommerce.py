"""
    3. An e-commerce platform needs to validate and reserve inventory when a customer places an order.
Before confirming the order, the system must:
1.	Check if all items are available in sufficient quantity 
2.	If available, reserve (deduct) stock 
3.	If not, reject the order with proper reasons
Sample Input Data:
Order Data:
{
  "items": [
    {"name": "Laptop", "qty": 1},
    {"name": "Mouse", "qty": 2}
  ]
}

Inventory Data:
{
  "Laptop": 5,
  "Mouse": 1,
  "Keyboard": 10
}

Step 1: Create a function 
Step 2: Check Order is dict or items key not in order then raise ValueError
Step 3: Inv data is dict or not then raise ValueError
Step 4: If Invaild item in order then Store at in New Variable
Step 5: Create a loop to check order not name or  Qty is int and greater than 0 otherwise raise ValueError
Step 6: Inv Name not in Inv data then store in New Variable
Step 7: Check Order Qty is greater than Inv Qty then store in New Variable
Step 8: If any issue reject order with proper reasons
Step 9: Reserve stock
Step 10: Return reserved stock details

    """

#step 1: Create a function
def val_and_res_order(order, inventory):
    #Step 2: Check Order is dict or items key not in order then raise ValueError
    if (type(order) != dict) or "items" not in order:
        raise ValueError("Invalid order data")
    
    #Step 3: Inv data is dict or not then raise ValueError
    if type(inventory) != dict:
        raise ValueError("Invalid inventory data")
    
    #Step 4:If Invaild item in order then Store at in New Variable
    invalid_items = []
    for item in order["items"]:
        if "name" not in item or "qty" not in item:
            invalid_items.append(item)
    if invalid_items:
        raise ValueError("Invalid items in order:", invalid_items)
    
    #Step 5: Create a loop to check order not name or  Qty is int and greater than 0 otherwise raise ValueError
    for item in order["items"]:
        if not isinstance(item["name"], str) or not isinstance(item["qty"], int) or item["qty"] <= 0:
            raise ValueError("Invalid item name or quantity:", item)
    
    #Step 6: Inv Name not in Inv data then store in New Variable
    unavailable_items = []
    for item in order["items"]:
        if item["name"] not in inventory:
            unavailable_items.append(item["name"])
    if unavailable_items:
        raise ValueError("Unavailable items in inventory:", unavailable_items)  
    
    #Step 7: Check Order Qty is greater than Inv Qty then store in New Variable
    insufficient_stock = []
    for item in order["items"]:
        if item["name"] in inventory and item["qty"] > inventory[item["name"]]:
            insufficient_stock.append(item["name"])
    if insufficient_stock:
        raise ValueError("Insufficient stock for items:", insufficient_stock)
    
    #Step 9:Reserve stock
    reserved_stock = {}
    for item in order["items"]:
        reserved_stock[item["name"]] = item["qty"]
        inventory[item["name"]] -= item["qty"]

    #Step 10: Return reserved stock details
    return reserved_stock


Order={
  "items": [
    {"name": "Laptop", "qty": 1},
    {"name": "Mouse", "qty": 2},
    # {"name": "mobile", "qty": 1}
  ]
}
Inventory={
  "Laptop": 5,
  "Mouse": 1,
  "Keyboard": 10
}


print(val_and_res_order(Order, Inventory))  
# Expected Output: ValueError: Insufficient stock for items: ['Mouse']

