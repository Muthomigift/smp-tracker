#CONTACT BOOK
contacts = [{"name":"James Omondi","phone":"0712345678","skill":"welding","city":"Nairobi"},
            {"name":"Sandra Weru","phone":"0723456789","skill":"tiling","city":"Mombasa"},
            {"name":"Patrick Njiru","phone":"0734567890","skill":"phone repair","city":"Nairobi"},
            {"name":"Grace Achieng","phone":"0745678901","skill":"copy writting","city":"Kisumu"},
            {"name":"Brian Kamau","phone":"075679012","skill":"upholstery","city":"Nairobi"}]
#display all contacts
print("=====CONTACT BOOK=====")
print("Contacts stored:", len(contacts))
for i,contact in enumerate(contacts):
    print(f"\n{i+1}.{contact['name']}")
    print(f"  Phone :{contact['phone']}")
    print(f"  Skill :{contact['skill']}")
    print(f"  City  :{contact['city']}")
#adding a new contact with append
new_contact ={"name":"Kelvin Mwangi","phone":"0712345678","skill":"beekeeping","city":"Machakos"}
contacts.append(new_contact)
print("\nNew contact list:", contacts)
print("\nContacts stored after adding one:",len(contacts))
print("\nNew contact:", contacts[-1])
#search by city
print("\n=====NAIROBI CONTACTS=====")
for contact in contacts:
    if contact["city"] == "Nairobi":
        print(f"{contact['name']} | {contact['phone']} | {contact['skill']}")

