# Find the largest element without using max().
# Input: [4, 8, 2, 9, 1] → Output: 9


lst = [4, 8, 2, 9, 1]

maxi = lst[0]


for i in lst:
    if(maxi<i):
        maxi = i
max = max(lst)        
print(maxi)

