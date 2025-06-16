#a program to check the sum f two numbersprovided by user sum of odd
def add(a,b):
    #TODO find the sum and return value
    return (a+b)

def check_even(number):
        #TODO how to handle try cach
    if number %2==0:
        return True
    else:
        return False
            

 #TODO ask two numbers from user
first_number=int (input("Enter first number\n"))
second_number=int (input("Enter Second number\n"))

 #TODO find the sum  using add function
sum= add(first_number, second_number)
 #TODO check the sum is even or not 
if check_even(sum):
    print ("Even")
else:
    print ("odd")
 

