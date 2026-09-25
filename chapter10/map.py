# map example
from functools import reduce
l = [1,2,3,4,5,6]
sq = lambda x:x*x
sqList = map(sq,l)
print(list(sqList))

# filter

def even(n):
    if(n%2!=0):
       return False
    else:
       return True

onlyeven = filter(even,l)
print(list(onlyeven))

# reduce

sum = lambda c,d: c+d

print(reduce(sum,l))

    