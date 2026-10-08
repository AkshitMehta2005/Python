# 6. Remove duplicates from a list.Input: [1, 2, 2, 3, 1] → Output: [1, 2, 3]
lst = [1, 2, 2, 3, 1] 

# method 1
s = set(lst)
new_lst = list(s)
print(new_lst)


# method 2

result = []

for i in lst:
    if i not in result:
        result.append(i)
        
print(result)


