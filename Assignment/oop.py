class Teacher:#creating Class
    def __init__(self,name,age):#initialzing the attributes of class
        self.__name = name# making the attributes privates
        self.__age = age
    def set_name(self,name):
            self._name= name
            #using setter method to set tha value in private attributesclerxc
    def  get_name(self):
                return self.__name       
    def give_assignment(self):#Craeting the behaviour of a class
        print("complete the assignment")       
Teacher1= Teacher("sunil",25)#creating object of the class
#accessing private attributes pf class is not allowed 
#print(Teacher1.name) 
#print(Teacher1.age) # not allowed
#calling the function of the class
Teacher1.give_assignment()
Teacher1.set_name("janak")
print(Teacher1.get_name())
      
    
