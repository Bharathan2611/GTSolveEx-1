Core Python Excercises:
Points to remember:
•	Validate errors in input according to problem statement.
•	Write Clean functions
•	Modularise code wherever needed.


1.Create a python function to generate employee salary using flexible inputs. Validate inputs and outputs wherever necessary. 
Inputs:
•	Base Salary – (required)
•	Allowances, tax - optional
Output:
•	Return Salary

2. Create a function that calculates total cart value.

•	Accept unlimited product prices 
•	Apply optional discount 
Output:
•	Return Total Price

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

4.	To the above problem statement create a function to filter products that are in stock and out of stock.

5.	Create decorator that:
•	Logs inputs 
•	Logs outputs 
•	Returns structured dict


6.	Create a function to generate the same coupon code for all users using map and lambda functions.

Sample Input:
[
{user:”alice”,coupon:””},
{user:”BOB”,coupon:””}
]
Sample Output:

[
{user:”alice”,coupon:”NEWUSER”},
{user:”BOB”,coupon:”NEWUSER”}
]

7.Create a logger decorator to log function name , number if args , number of kwargs, and arguments passed to the function.

8.Create a generator function to read from a large size file.

9.Sample Data :

orders = [
{"id": 1, "amount": 200},
{"id": 2, "amount": 500},
{"id": 3, "amount": 100},
{"id": 4, "amount": 50},

]

•	Filter orders above 150
•	For those orders add the status as processed
•	Parse the output to JSON format

10.Write a function to read a JSON file and convert to dict. 

11.Todo Application:

Write a well structured clean code for task manager application.
Mock Data:
https://jsonplaceholder.typicode.com/todos




