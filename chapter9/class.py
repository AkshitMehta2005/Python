class train:
    name = "Raj"  # class attribute
    journey = "dehradun to joshimath"
    trainNo = 123
    
    
# object 1
a = train()
print(a.name,a.journey,a.trainNo)
    
    
# object 2
b = train()
b.name = "akshit"  # instance atribute
b.journey = "Dehradun to Noida"
b.trainNo = 1047
print(b.name,b.journey,b.trainNo)
    