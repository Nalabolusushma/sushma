class person:
    name = "sushma"
    age = "22"
    job = "devops engineer"
    def info(self): #info method provides a information of the datapoints
     print(f"{self.name} is a {self.job}")
obj = person()
obj.name = "suchi"

obj1 = person()
obj.info() # you have that method with the object
obj1.info()