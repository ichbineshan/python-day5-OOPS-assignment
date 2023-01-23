#Create arithmetics class to calculate avg, mean, mode and standard deviation
from statistics import stdev
import time

class Arithmetics:
    
    def __init__(self,listl):
        self.originallist=listl[:]      #original copy to preserve user input sequence
        self.l=listl                    #for all calculation purposes, list will be sorted 
        listl.sort()
    
    def mean(self):
        print( f"Mean of {self.originallist} is : {sum(self.l)/len(self.l)}\n")        
        
    def median(self):
        n=len(self.l)
        
        if n%2==0:
            m1=self.l[n//2]
            m2=self.l[n//2 -1]
            m= (m1+m2)/2
        else :
            m=self.l[n//2]    
            
        print( f"Median of {self.originallist} is : {m}\n")        
        

    def mode(self):
        cnt= [self.l.count(n) for n in self.l]
        d=dict(zip(self.l,cnt))
        d2={key for (key,value) in d.items() if value == max(cnt) }
        print( f"Mode of {self.originallist} is :", list(d2),"\n")     
        
        
    def standardDeviation(self):
        # xs=list(map(float,self.l))
        # mean = sum(xs) / len(xs)   # mean
        # var  = sum(pow(x-mean,2) for x in xs) / len(xs)  # variance
        # std  = sqrt(var)  # standard deviation    
        print(f"Standard Deviation of {self.originallist} is :", stdev(self.l),"\n")
        
        
lis=[]

n=int(input("How many total numbers would you like to perform operation on? "))
for i in range(n):
    lis.append(int(input(f"Enter the number (Remaining number(s)={n-i}) : ")))
    
obj= Arithmetics(lis)

while True:
    print("Choose an Operation -\n 1 - Mean\n 2 - Median \n 3 - Mode \n 4 - Standard Deviation \n Type E to exit")
    inp=input()
    if inp in ('E','e'):
        break
    option=int(inp)
    match option:
        case 1:
            obj.mean()           
        case 2:
            obj.median()    
        case 3:
            obj.mode()
        case 4:
            obj.standardDeviation()         
    time.sleep(1)
