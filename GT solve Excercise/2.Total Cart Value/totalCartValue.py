"""
2. Create a function that calculates total cart value.

•	Accept unlimited product prices 
•	Apply optional discount 
Output:
•	Return Total Price

Accept unlimited(multiple Values) prod prices using *args --> store more values in tuple
Apply optional disc using **kwargs --> store more values in dict

Step 1: Create a function
step 2: Check if prices is None then raise ValueError
step 3: Remove any ("$",",") reomve from price values convert into float -- to list
Step 4: Each Price Validation Check (minus or string value) then raise ValueError
Step 5: Discount less than 0 or greater than 100 then raise ValueError 
Step 6: discount percentage to discount amount
Step 7: Total Price = sum of product prices - discount
Step 8: Return Total Price
    """
#Step 1: Create a function

def cal_total_price(*prices,disc=0):
    #step 2: Check if prices is None then raise ValueError
    if not prices:
        raise ValueError("at least one prdt price required")
    
    #Step 3: Remove any ("$",",") reomve from price values convert into float -- to list
    remove_Symbol=[]
    for p in prices:
        if "$" in str(p) or "," in str(p):
            p=p.replace("$", "").replace(",", "")
            remove_Symbol.append(float(p))
        try:
            value = float(p)
            remove_Symbol.append(value)
        except ValueError:
                raise ValueError(f"Invalid price value: {p}")
                
    #Step 4: Each Price Validation Check (minus or string value) then raise ValueError
    for price in remove_Symbol:
        if price < 0:
            raise ValueError("Price cannot be negative")
    
    #Step 5: Discount less than 0 or greater than 100 then raise ValueError 
    if disc < 0 or disc > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    #Step 6: discount percentage to discount amount
    total_price = sum(remove_Symbol) #total price before disc  
    disc_amount = total_price * (disc / 100)
    
    #Step 7: Total Price = sum of product prices - discount
    final_price = total_price - disc_amount
    
    #Step 8: Return Total Price
    return final_price



print(cal_total_price(100, 200, 300, disc=10))  # Expected Output: 540.0
print(cal_total_price("$1,000", "$2,000", disc=20))  # Expected Output: 2400.0
print(cal_total_price("500", "1500", disc=15))  # Expected Output: 1700.0

    