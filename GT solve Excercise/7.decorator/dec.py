""" 
7.Create a logger decorator to log function name , number if args , 
number of kwargs, and arguments passed to the function.

step 1: Create a dec func 
step 2: Create a wrap function inside decorator to log func name, no of args
and kwargs, and arguments passed to the function
step 3: Call the original function and return the result
step 4: Return the wrap func

"""

#Step 1: Create a dec func
def logger(func):
    #step 2: Create a wrap function inside decorator to log func name, no of args
    # and kwargs, and arguments passed to the function
    def wrapper(*args, **kwargs):
        print(f"Function Name: {func.__name__}")
        print(f"Number of args: {len(args)}")
        print(f"Number of kwargs: {len(kwargs)}")
        print(f"Arguments passed: args={args}, kwargs={kwargs}")
        
        #step 3: Call the original function and return the result
        result = func(*args, **kwargs)
        return result
    
    #step 4: Return the wrap func
    return wrapper

#Eg. usage
@logger
def add(a, b, c=0):
    return a + b + c
result = add(1, 2, c=3)
print(result)

@logger 
def GTsolveInter(name, age):
    return {"name": name, "age": age}

#Bharathan
result = GTsolveInter(name="Bharathan", age=25)
print(result)

#Vijayalakshmi
result = GTsolveInter(name="Vijayalakshmi", age=22)
print(result)
