# def my_gen():
#     for i in range(5):
#         yield i;
        
# gen = my_gen()

# for i in gen:
#     print(i)
    
def my_gen():
    for i in range(5):
        yield i

gen = my_gen()


for i in gen :
    print(i)    
    
    
    
    
    