class Employee:
    def __init__(self,name): 
       self.name = name
    def __len__(self):    
     i = 0
     for c in self.name:
        i = i+1
     return i 
    def __str__(self):
       return f"name of employee {self.name} is str" 
    def __repr__(self):
       return f"name of employee {self.name} is repr" 
    def __call__(self):
       print("Hy")

e = Employee("sushma")
print(e)
print(len(e))
e()