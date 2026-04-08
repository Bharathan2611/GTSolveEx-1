"""
6.	Create a function to 
    generate the same coupon code for all users using map and lambda functions. 

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


Step 1: Create a func
Step 2: list of user name and Coupon code
Step 3: Create lambda dunc to generate cooupon code for all user
    """

#Step 1: Create a func
def gen_coupon(users):
    #Step 2: list of user name and Coupon code
    if not isinstance(users, list):
        raise ValueError("Invalid input data")
    
    # for u in users:
    #     if "user" not in u or "coupon" not in u:
    #         raise ValueError("Invalid user data:", u)

    #Step 3: Create lambda dunc to generate cooupon code for all user
    generate_coupon = lambda customerName: {"user": customerName["user"], "coupon": "NEWUSER"}
    return list(map(generate_coupon, users))


input=[
    {"user": "Suganya", "coupon": ""},
    {"user": "Bharathan", "coupon": ""},
    {"user": "Vijayalakshmi", "coupon": ""},
    {"user": "Durai", "coupon": ""}
]

print(gen_coupon(input))

"""
    output:
    [{'user': 'Suganya', 'coupon': 'NEWUSER'}, 
    {'user': 'Bharathan', 'coupon': 'NEWUSER'},
    {'user': 'Vijayalakshmi', 'coupon': 'NEWUSER'}, 
    {'user': 'Durai', 'coupon': 'NEWUSER'}]

"""