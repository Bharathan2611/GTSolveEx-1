
""" 
8.Create a generator function to read from a large size file

Step 1: Create a gen func
Step 2: Use with open to read the file
Step 3: Use yield return one line 

"""

#Step 1: Create a gen func
def read_large_file(file_path):
    #Step 2: Use with open to read the file
    try :
        with open(file_path, 'r') as file:
            #Step 3: Use yield return one line 
            for line in file:
                yield line 
    except FileNotFoundError:
        print(f"File not found: {file_path}")

#Example usage
file_path = 'GT solve Overall About Company.txt'  

#print(list(read_large_file(file_path)))

for line in read_large_file(file_path):
    print(line)  


    """  Output:
    Overall About Company
* GT Solve Pvt Ltd is an engineering + manufacturing service company
* Focus: AI-based design, automation, tooling & manufacturing
* Works with global clients (mobility & industrial sector)
* Goal: Deliver high-quality, practical engineering solutions

1. CSR & Sustainability
* Focus on environment protection & sustainable manufacturing
* Provide safe & inclusive workplace
* Support community development & education
* Promote ethical sourcing
* Aim to reduce carbon footprint & use renewable energy

2. Code of Ethics
* Work with honesty & transparency
* Follow laws & regulations
* Strict no bribery policy
* Protect data & confidentiality
* No discrimination in workplace
* Avoid conflict of interest

3. Anti-Fraud & Anti-Corruption
* Zero tolerance for fraud & corruption
* Maintain clear financial records
* No bribes, kickbacks, illegal benefits
* Report any suspicious activity immediately
* Violations ? strict action/legal consequences

4. Quality Policy
* Focus on engineering excellence
* Deliver high performance & reliable solutions
* Follow global standards (ISO, IATF, CE)
* Continuous improvement & innovation
* Strong supplier collaboration & quality checks

5. Standards & Compliance
* Aligns with:
o ISO 9001 (Quality)
o IATF 16949 (Automotive)
o ISO 14001 (Environment)
* Ready for global market & supply chain requirements

6. Privacy & Data Protection
* Protect client & company data
* Use data only for valid business purposes
* Limit access (only authorized people)
* Maintain security & confidentiality
* Follow Indian + international data laws
    """


