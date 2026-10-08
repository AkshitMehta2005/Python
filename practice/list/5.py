# 7. Find the second-largest distinct element.
# Input: [10, 5, 8, 10, 7] → Output: 8

lst = [4, 8, 2, 9, 1]

maxi = lst[0]
for i in lst:
    if(maxi<i):
        maxi = i
      
print(maxi)
