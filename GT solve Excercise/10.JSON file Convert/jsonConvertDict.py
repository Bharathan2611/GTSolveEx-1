""" 
10.Write a function to read a JSON file and convert to dict. 

step 1: Create a function
step 2: Check file is valid or not then raise ValueError
step 3: Read JSON file convert to dict json module
step 4: Return dict data
"""

import json
#Step 1: Create a function
def json_to_dict(file_path):
    #Step 2: Check file is valid or not then raise ValueError
    try:
        with open(file_path, 'r') as file:
            #Step 3: Read JSON file convert to dict json module
            data = json.load(file)
            #Step 4: Return dict data
            return data
    except FileNotFoundError:
        raise ValueError("File not found")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")

# Example usage
dict_data = json_to_dict('data.json')
print(dict_data)

# dict_data = json_to_dict('invalid.json')  #File not found
# print(dict_data)

dict_data = json_to_dict('GT solve Overall About Company.txt') #Invalid JSON format
print(dict_data)