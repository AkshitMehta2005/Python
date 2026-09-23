d1 = {
    "OutLier":"100",
    "Latest":"190",
    "Avg":"120",
    "Lowest":"20",
    "Highest":"70"
}


print(d1.items()) #  this method convert all data into tuple
print(d1.keys())
d1.update({"Avg":"80","New":"9009"});  # this help to add and update new value in dictonary
print(d1)
# print(d1["Avg"])  
print(d1.get("Avg")) 