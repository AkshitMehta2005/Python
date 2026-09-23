# () -> immutable
# [] -> mutable
# "" -> immutable 


a = []
a.append(1);
a.append(3);
a.append(4);
a.append(1);
b = int(input("Enter the number b "));
a.append(b)
print(sum(a))