class train:
    name = "Raj"  # class attribute
    journey = "dehradun to joshimath"
    trainNo = 123
    
    def Greet(self):
        print(f"welcome to the train {self.name}.")
    def func(self):
        print("Welcome to the Train")
    @staticmethod
    def destination():   
        print(f"static method do not need any object to define") 
        
        
        
a = train()
a.Greet()
a.destination()



