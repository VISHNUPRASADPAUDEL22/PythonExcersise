from phone import Phone
#TODO how do i implement my inventory?
phone_inventory=[]

#TODO add a phone in inventory
#TODO ask the phone details from the user before adding the phone to inventory
phone = Phone ("S20","samsung",5000,"32GB", "30")
phone1 = Phone ("S63","samsung",8000,"32GB", "30")

phone_inventory.append(phone)
phone_inventory.append(phone1)
print(phone_inventory)

#TODO view details of phone
#TODO how do i show information of the phone that the user wants.
for phone in phone_inventory:
    
    print(f"phone Model: {phone.get_model()}")
    print(f"phone Brand: {phone.get_brand()}")
#TODO update detail of phones
#TODO delete a phone

#TODO how to allow user to do the operations?
