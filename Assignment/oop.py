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
class Math_Teacher(Teacher):
    def __init__(self,name,age,strict):
       super().__init__(name,age)
       self.strict= strict
    def set_strict(self,stric):
        self.__strict= strict 
        
    def get_strict (self):
        return self.__strict
       
class English_teacher(Teacher):
    def __init__(self,name,age,polite):
       super().__init__(name,age)
       self.__polite= polite
       
       def set_strict(self,polite):
        self.__strict= polite 
        
    def get_strict (self):
        return self.__strict

#creating object math teacher
math_teacher1= Math_Teacher("sunil",25,"very strict")#creating object of the class
math_teacher1.give_assignment()          
#accessing private attributes pf class is not allowed 
#print(Teacher1.name) 
#print(Teacher1.age) # not allowed
#calling the function of the class
print(math_teacher1.get_name())
math_teacher1.give_assignment()



english_teacher1= English_teacher("English_Teacher",28," very Polit")
english_teacher1.give_assignment()
print(english_teacher1.get_name())    
english_teacher1.give_assignment() 
