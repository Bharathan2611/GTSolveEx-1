
"""
    Create a python function to generate employee salary using flexible inputs. Validate inputs and outputs wherever necessary. 
        Inputs:
        •	Base Salary - (required)
        •	Allowances, tax - optional
        Output:
        •	Return Salary

        
    Step 1: Create a function
    Step 2:Sal must be required 
    Step 3:Al and tax default value =0 because optional
    Step 4:Salary is None then raise ValueError
    Step 5:I am user input Value may be given in 10K or 1M 
          I convert into numerical then datatypes Convert into float 
    Step 6:Check sal,al and tax should be int or float otherwise raise TypeError
    Step 7:Total Salary = sal + al - tax
    step 8:May be minus value after the Caluation so I check total Salary 
    Step 9:Return Total Salary 
    """ 
#Step 1: Create a function
def cal_Salary(sal,al=0,tax=0):

    #Step 4:Salary is None then raise ValueError 
    if sal is None:
        raise ValueError("Salary is required")
    
    #Step 5:I am user input Value may be given in 10K or 1M 
    # I convert into numerical then datatypes Convert into float
    if "k" in sal or "K" in sal:
        sal = sal.replace("k", "").replace("K", "")
        sal = float(sal) * 1000

    elif "m" in sal or "M" in sal:
        sal = sal.replace("m", "").replace("M", "")
        sal = float(sal) * 1000000
    else: 
        sal = float(sal)

    #Step 6:Check sal,al and tax should be int or float otherwise raise TypeError
    if type(sal) not in [int,float]:
        raise TypeError("Salary should be int or Float value")
    
    #tax percentage to tax amount
    tax=tax/100*sal
    
    #Step 7:Total Salary = sal + al - tax
    total_salary = sal + al - tax

    #step 8:May be minus value after the Caluation so I check total Salary
    if total_salary < 0:
        raise ValueError("Total Salary cannot be minus value")
    
    return total_salary

#input 
sal=input("Enter the Salary :")
al=float(input("Enter the Allowance :"))
tax=float(input("Enter the Tax percentage :"))


#call function
print("Total Salary:",cal_Salary(sal,al,tax))