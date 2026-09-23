# print the program of multiplicatuion using -> for loop

# n = int(input("Enter the number: "))

# for i in range(1, 11):
#     print(f"{n} * {i} = {n * i}")
    
    
# check prime number or not


# n = int(input("Enter the number: "))

# if n <= 1:
#     print("Not Prime Number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime Number")
#             break
#     else:
#         print("Prime Number")
        
        
n = int(input("Enter the number: "))
prod = 1
for i in range(1,n+1):
    prod = i*prod
    
print(prod)
    
       