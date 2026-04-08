"""9.Sample Data :

orders = [
{"id": 1, "amount": 200},
{"id": 2, "amount": 500},
{"id": 3, "amount": 100},
{"id": 4, "amount": 50},

]

•	Filter orders above 150
•	For those orders add the status as processed
•	Parse the output to JSON format 

Step 1: create func to filter order above 150
Step 2: Add status as processed for those orders
Step 3: Parse the output to JSON format

"""

import json 

#Step 1: create func to filter order above 150
def filter_orders(orders):
    #Step 2: Add status as processed for those orders
    processed_orders = []
    for order in orders:
        if order["amount"] > 150:
            order["status"] = "processed"
            processed_orders.append(order)
    #Step 3: Parse the output to JSON format
    return json.dumps(processed_orders, indent=4)

orders = [
    {"id": 1, "name": "Bharathan", "amount": 200},   
    {"id": 2, "name": "Vijayalakshmi", "amount": 500},
    {"id": 3, "name": "Viji", "amount": 100},
    {"id": 4, "name": "Bharath", "amount": 50},
]

print(filter_orders(orders))
"""
    output:
    [
        {
            "id": 1,
            "name": "Bharathan",
            "amount": 200,
            "status": "processed"
        },
        {
            "id": 2,
            "name": "Vijayalakshmi",
            "amount": 500,
            "status": "processed"
        }
    ] """
