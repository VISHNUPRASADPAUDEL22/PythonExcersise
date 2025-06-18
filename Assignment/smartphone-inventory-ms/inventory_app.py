from phone import Phone
#TODO how do i implement my inventory?
phone_inventory=[]

#TODO add a phone in inventory
#TODO ask the phone details from the user before adding the phone to inventory
#TODO need to handle
def add_phone():
    model=str(input("Enter the phone model:"))
    brand=str(input("Enter the phone brand:"))
    price=int(input("Enter the phone price:"))
    storage=str(input("Enter the phone storage:"))
    quantity=int(input("Enter the phone quantity:"))

    phone = Phone (model,brand,price,storage,quantity)

    phone_inventory.append(phone)
    print(phone_inventory)

#TODO view details of phone
#TODO how do i show information of the phone that the user wants.
def view_phone_details():
    for phone in phone_inventory:
    
        print(f"phone Model: {phone.get_model()}")
        print(f"phone Brand: {phone.get_brand()}")
#TODO update detail of phones
#TODO delete a phone
#TODO how to allow user to do the operations?
#TODO how to let the user program as much as they want
#TODO how to let user exit the program. 
print("Enter 1 to add phone:")
print("Enter 2 to view details:")
option=int(input("choose and option"))
if(option==1):
    add_phone()
elif(option==2):
    view_phone_details()



