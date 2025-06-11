for i in range ( 2,5):

    try:
        age = int(input("enter your age "))
        if age<15:
                print(f"(age) is miner")
        elif age>=15:
                    print(f"(age) is Old")
        else:
                    print("Enter a proper age")
    except:
        print("please give number")
    run=input("dp you want to contiune??(Y/N)\n")
    
