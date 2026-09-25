a = int(input("Enter a Number"))

match a:
    case 1:
        print("You are fired")
    case 2:
        print("You got promotion")
    case 3:
        print("Now You got for job switch")
    case _:
        print("By default")