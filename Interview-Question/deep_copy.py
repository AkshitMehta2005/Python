from copy import deepcopy

l1 = [1,2,[3,4],5,6]
# deep copy

l2 = deepcopy(l1)

l2[0] = 0
l2[2].append(10)


print(l1)
print(l2)