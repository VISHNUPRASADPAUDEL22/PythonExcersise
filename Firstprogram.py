
try:
    age = int(input("enter your age "))#Exception
    if age<15:
        print(f"(age) is miner")
    elif age>=15:
        print(f"(age) is Old")
    else:
        print("Enter a proper age")
except:
    print("please give number")