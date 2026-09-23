# __init__() Constructor
# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.

class train:
    name = "Raj"  # class attribute
    journey = "dehradun to joshimath"
    trainNo = 123
    
    def __init__(self):  # dunder function 
        print(f"hello it is automatically run when the object is created then called")
    
    @staticmethod
    def destination():   
        print(f"static method do not need any object to define") 
        
        
a = train()
print(a.name)
        
        