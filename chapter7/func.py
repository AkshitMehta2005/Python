# def hello():
#     print("helllo")


def avg():
    a = int(input("Enter the 1st number"));
    b = int(input("Enter the 2st number"));
    c = int(input("Enter the 3st number"));
    print(a+b+c/3);
    
    
def hello(name,wish):
    print(wish,name)    
    
    
hello("akshit","Good afternoon ")
# avg()


# Default Parameter Value
# We can have a value as default as default argument in a function. 

def hello(name,wish="Good Morning"):
    print(wish,name)
    
    
hello("akshit") # here by default wish argument set 
hello("akshit","hello")