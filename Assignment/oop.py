class Teacher:#creating Class
    def __init__(self,name,age):#initialzing the attributes of class
        self.name = name
        self.age = age
        
    def give_assignment(self):#Craeting the behaviour of a class
        print("complete the assignment")       
Teacher1= Teacher("sunil",25)#creating object of the class
#accessing the attributes of class
print(Teacher1.name) 
print(Teacher1.age)
#calling the function of the class
Teacher1.give_assignment()
      
    
