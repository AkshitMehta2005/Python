

# def test(*args,**kwargs):
    
#     print("this is a position argument: ")
#     for arg in args:
#         print(arg)

#     print("\n key- val pair in dictonary")
#     for key,val in kwargs.items():
#         print(f"{key,val}")
        
# test(1,2,3,4,name="akshit",age=22)


def test(*args,**kwargs):
    print(args)
    
    print(kwargs)
    
    
test(1,2,3,name="akshit",age=21)
     