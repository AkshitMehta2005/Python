# 4. Reverse a list without using reverse() or reversed().


lst =  [1,2,3,4]
n = len(lst)

for i in range(n//2):
    a = lst[i]
    lst[i] = lst[n-i-1]
    lst[n-i-1] = a
    
print(lst)
