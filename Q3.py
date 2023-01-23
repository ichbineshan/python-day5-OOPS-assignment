# # Create a program to validate the age of the voter with the help of custom exception. 
# # Voters whose age is less than 18 should not be allowed to vote.

from datetime import date

class MyCustomException(Exception):
   pass

class Validator:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    
    def result(self):
        if self.age>=18:
            print(f"Congratulations {self.name.split()[0]}, You are eligible to vote!")   
        else:
            raise MyCustomException(f"Sorry {self.name.split()[0]}, You are not yet eligible to vote. Please retry next year.")    
                               
            
def dobtoage(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
                
name=input("Enter your name : ")
birth=input("Enter your Age or Date of Birth in DD-MM-YYYY: ")

if len(birth)<=3 and len(birth)!=0:
    age=int(birth)
else:
    d,m,y=map(int,birth.split("-"))
    age=dobtoage(date(y,m,d))
      
obj = Validator(name,age)
try:
    obj.result()
except MyCustomException as e:
    print(e)
    
    

