from phone import Phone
#TODO how do i implement my inventory?
phone_inventory =  [Phone("model","Brand",223,"storage",223),
                    Phone("test1","teastBrand1",222223, "teatstorage1",456),    
                    Phone("test2","teastBrand2",22789, "teatstorage2",456)]
#TODO add a phone in inventory
#TODO ask the phone details from the user before adding the phone to inventory
#TODO need to handle
#TODO how to privent duplicate phone model number??
def add_phone():
    model=str(input("Enter the phone model:"))
    brand=str(input("Enter the phone brand:"))
    price=int(input("Enter the phone price:"))
    storage=str(input("Enter the phone storage:"))
    quantity=int(input("Enter the phone quantity:"))

    phone = Phone (model,brand,price,storage,quantity)

    phone_inventory.append(phone)
    # print(phone_inventory)

#TODO view details of phone
#TODO how do i show information of the phone that the user wants.
def view_phone_details():
    for phone in phone_inventory:
    
        print(f"phone Model: {phone.get_model()}")
        print(f"phone Brand: {phone.get_brand()}")
        print(f"phone storage: {phone.get_storage()}")
        print(f"phone Price: {phone.get_price()}")
        print(f"phone Quantity: {phone.get_quantity()}")
        print("\n")
#TODO update detail of phones
def update_phonedetails():
    model_number_to_update=input("enter the phone number:")

    for phone in phone_inventory:
        if model_number_to_update == phone.get_model():
            new_model_number= input("Enter Model Number:")
            new_brand=input("Enter brand:")
            phone.set_model(new_model_number)
            phone.set_model(new_brand)
            print(f"{model_number_to_update} has been updated")
            return     
        else:
            print(f"{model_number_to_update} record not found")
            return
                       
#TODO delete a phone
def delete_phone():
    model_number_to_delete=input("Enetr the phone model to delete")
    for phone in phone_inventory:
        if model_number_to_delete == phone.get_model():
            phone_inventory.remove(phone)
            print(f"{model_number_to_delete} has been removerd from the record")
            return
        else:
            print(f"{model_number_to_delete} not found the record")
        
        
       
    
#TODO how to allow user to do the operations?
#TODO how to let the user program as much as they want
#TODO how to let user exit the program. 
    #def menu():
while(True):
    print("Enter 1 to add phone:")
    print("Enter 2 to view details:")
    print("Enter 3 to update phone details:")
    print("Enter 4 to remove phone:")
    print("Enter 6 to Exit:")
    option=int(input("choose and option"))
    if(option==1):
        add_phone()
    elif(option==2):
        view_phone_details()
    elif(option==3):
        update_phonedetails()
    elif(option==4):
        delete_phone()
    elif(option==5):
        print("thank you, see you again")
        break
    else: 
        print("enetr the options from (1-to 5)\n")
        





