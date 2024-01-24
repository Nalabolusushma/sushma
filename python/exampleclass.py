class person:
    name = "sushma"
    age = "22"
    job = "devops engineer"
obj = person()
print(obj.name) # you have to declare the variables with the object name
obj.name = "suchi"
#above obj.name = "suchi" give nothing bcoz we give to the inside the obj
obj1 = person()
obj1.name = "suchi"
print(obj1.name)
print(obj1.age) 