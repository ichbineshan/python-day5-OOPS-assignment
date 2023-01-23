# Create a program to check eligibility of the person for loan  with the help of oops concepts and exception handling.
# Person whose salary is less than 10K/ Month will not be eligible for the loan.


class LowCreditScoreException(Exception):
    pass
class LowSalaryException(Exception):
    pass

class Eligible:
    
    def __init__(self,name,salary,creditscore):
        self.name=name
        self.salary=salary
        self.creditscore=creditscore
    
    def checkIfEligible(self):
        if self.salary<10000:
            raise LowSalaryException(f"Sorry {self.name.split()[0]}, according to the Minimum Salary Requirement (MSR) criterion, you are ineligible for loan.")
        elif self.creditscore<650:
            raise LowCreditScoreException(f"Sorry {self.name.split()[0]}, according to the Minimum Credit Score (CIBIL) Criterion, you are ineligible for loan.")
        else:
            print(f"Congratulations {self.name.split()[0]}, you are eligible for loan.")
            
        #Note: We can raise the same exception more than once with different messages also.
        #Example: raise IneligibilityException("Sorry Low Credit Score") and raise IneligibilityException("Sorry, Low Salary")
        
name=input("Enter your name : ")
salary=int(input("Enter your salary per month (in digits) : "))   
creditscore=int(input("Enter your credit score (CIBIL) : "))         
obj= Eligible(name,salary,creditscore)

try:
    obj.checkIfEligible()
except (LowSalaryException,LowCreditScoreException) as e:
    print(e)                