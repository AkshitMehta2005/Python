# Find the sum of all elements in a list.
from functools import reduce


# method 1
lst = [1,2,3,4]
sum = 0
for i in lst:
    sum = sum+i
    
print(sum)

# method 2
a = reduce(lambda x,y:x+y , lst)

print(a)


