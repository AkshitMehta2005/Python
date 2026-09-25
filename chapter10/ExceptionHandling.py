try:
    a = int(input("Enter a number"))
    print(f"the number is {a}")
    
except Exception as e:
    print(e)
    
finally:
    print("I am final statement")
    