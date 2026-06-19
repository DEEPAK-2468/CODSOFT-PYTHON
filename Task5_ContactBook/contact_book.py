import os
fname=os.path.join(os.path.dirname(__file__), "Contacts.txt")

def load():
    contacts=[]
    if (os.path.exists(fname)):
        with open(fname,"r") as f:
            for contact in f:
                contacts.append(contact.strip().split("-"))
    return contacts

def add(contacts):
    print("\nEnter Contact details to Add:")
    name=input("Enter Contact Name: ")
    number=int(input("Enter Contact Number: "))
    email=input("Enter Contact Email: ")
    address=input("Enter Contact Address: ")
    contacts.append([name,number,email,address])
    print("Contact Added.")

def view(contacts):
    if not contacts:
        print("No contacts available.")
        return
    else:
        print("\nContact Details:")
        for contact in contacts:
            print(f"{contact[0]} - {contact[1]} - {contact[2]} - {contact[3]}")

def search(contacts):
    if not contacts:
        print("Contact list is Empty.")
        return
    else:   
        name=input("Enter name of the contact to search: ")
        for contact in contacts:
            if (name==contact[0]):
                print("Contact Details:")
                print(f"{contact[0]} - {contact[1]} - {contact[2]} - {contact[3]}")
                return
    print("Contact not Available.")
    
def update(contacts):
    if not contacts:
        print("Contact list is Empty.")
        return
    else:   
        name=input("Enter name of the contact to search: ")
        for contact in contacts:
            if (name==contact[0]):
                print("\nEnter Contact details to update (leave blank if no change needed):")
                new_name=input("Enter New Contact Name: ")
                new_number=input("Enter New Contact Number: ")
                new_email=input("Enter New Contact Email: ")
                new_address=input("Enter New Contact Address: ")
                if (new_name):
                    contact[0]=new_name
                if (new_number):
                    contact[1]=int(new_number)
                if (new_email):
                    contact[2]=new_email
                if (new_address):
                    contact[3]=new_address
                print("Contact Updated.")
                return
    print("Contact not Available.")

def delete(contacts):
    if not contacts:
        print("Contact list is Empty.")
        return
    else:   
        name=input("Enter name of the contact to delete: ")
        for i in range(len(contacts)):
            if (name==contacts[i][0]):
                contacts.pop(i)
                print("Contact Deleted.")
                return
    print("Contact not Available.")

def save(contacts):
    with open(fname,"w") as f:
        for contact in contacts:
            f.write(f"{contact[0]}-{contact[1]}-{contact[2]}-{contact[3]}\n")

contacts=load()
while True:
    print("\nMENU:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try:
        choice=int(input("Enter you choice: "))
        
        if (choice==1):
            add(contacts)
        elif (choice==2):
            view(contacts)
        elif (choice==3):
            search(contacts)
        elif (choice==4):
            update(contacts)
        elif (choice==5):
            delete(contacts)
        elif (choice==6):
            save(contacts)
            break
        else:
            print("Enter a Valid choice.")
            continue
        save(contacts)

    except ValueError:
        print("Enter a Valid Answer.")
