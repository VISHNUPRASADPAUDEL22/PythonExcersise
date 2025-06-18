#TODO creat a class name phone
#withprivate attributes brand, model, modelnumber,price,storage
#create setters and getters for the private attributes
class Phone:
    def __init__(self,model:str,brand:str,price: int,storage:str,quantity:int):
        self.__model=model
        self.__brand=brand
        self.__price=price
        self.__storage=storage
        self.__quantity=quantity
        
    def set_model(self,model:str):# Set for mobile Model
        self.__model= model
        
    def  get_model(self) -> str:  #Get for mobile Model
        return self.__model 
    
    def set_brand(self,brand:str): # Set for mobile Brand
        self.__brand= brand
        
    def get_brand(self) ->int :
        return self.__brand #Get for mobile Brand
    
    def set_price(self,price:int):# Set for mobile Price
        self.__price= price
        
    def get_price(self)->int:
        return self.__price  # Set for mobile Price
    
    def set_storage(self,Storage:str):# Set for mobile storage
        self.__storage= Storage
        
    def Set_storage(self)->str:
        return self.__storage  # Set for mobile storage
    
    def set__quantity (self,quantity:int):# Set for mobile storage
        self.__quantity= quantity
        
    def Set_quantity(self)->int:
        return self.__quantity  # Set for mobile storage
    
        
