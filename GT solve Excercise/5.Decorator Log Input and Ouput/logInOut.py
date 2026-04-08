"""
    5.	Create decorator that:
•	Logs inputs 
•	Logs outputs 
•	Returns structured dict

Step 1: Create a decorator function
Step 2: Create a wrapper func inside the decorator to log inputs and outputs
Step 3: Return dict
    """

# #Step 1: Create a decorator function
def log_input_output(func):
    def wrapper(*args, **kwargs):
        # Step 2: Log inputs
        print("Inputs: args=",args, "kwargs=",kwargs)
        
        # Call the original function and get the output
        output = func(*args, **kwargs)
        
        # Step 2: Log outputs
        print("Output:", output)
        
        # Step 3: Return structured dict
        return {
            "inputs": {"args": args,"kwargs": kwargs},"output": output
        }
    return wrapper

#Example for Args 
@log_input_output
def add(a, b):
    return a + b
result = add(7,9) 
print(result)

#Example for Kwargs
@log_input_output
def GTsolveInter(name,age):
    return {"name": name, "age": age}

#Bharathan
result = GTsolveInter(name="Bharathan",age=25)
print(result)

#Vijayalakshmi
result = GTsolveInter(name="Vijayalakshmi",age=22)
print(result)





