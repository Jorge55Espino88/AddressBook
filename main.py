from datetime import datetime

print("*** Address Book ***")

user = input("Please enter your name: ")
address_book = []


def view_contacts():
    print("*** Contacts ***")
    if address_book:
        for contact in address_book:
            print(f"""Id: {contact.get('id')}
            Name: {contact.get('name')}
            Last name: {contact.get('last_name')}
            Telephone: {contact.get('telephone')}
            Cellphone: {contact.get('cell_phone')}
            Email: {contact.get('email')}
            """)
    else:
        print("*** No contacts ***")


def especific_contact(id):
    for contact in address_book:
        if contact['id'] == id:
            print(f"""Id: {contact.get('id')}
            Name: {contact.get('name')}
            Last name: {contact.get('last_name')}
            Telephone: {contact.get('telephone')}
            Cellphone: {contact.get('cell_phone')}
            Email: {contact.get('email')}
            """)
            return

    print("Contact not found")



def add_contact():
    date = datetime.now().date()
    id = f"{date.year}{date.month:02d}{date.day:02d}-{len(address_book) + 1}"
    name = input("Please enter the name of the contact: ").strip()
    last_name = input("Please enter the last name of the contact: ").strip()
    telephone = input("Please enter the telephone number of the contact: ").strip()
    cell_phone = input("Please enter the cellphone number of the contact: ").strip()
    email = input("Please enter the email address of the contact: ").strip()
    if not name:
        print("Please enter a valid name")
        return
    if not last_name:
        print("Please enter a valid last name")
        return
    if not telephone or not telephone.isdigit():
        print("Please enter a valid telephone number")
        return
    if not cell_phone or not cell_phone.isdigit():
        print("Please enter a valid cellphone number")
        return
    if email and not  "@" in email:
        print("Please enter a valid email address")
        return

    new_contact = {"id": id, "name": name, "last_name": last_name, "telephone": telephone, "cell_phone": cell_phone, "email": email}
    address_book.append(new_contact)

    print("Contact added successfully")


def update_contact(id):
    for contact in address_book:
        if contact['id'] == id:
            name = input(f"New name ({contact['name']}): ").strip() or contact['name']
            last_name = input(f"New last name ({contact['last_name']}): ").strip() or contact['last_name']
            telephone = input(f"New telephone ({contact['telephone']}): ").strip() or contact['telephone']
            cell_phone = input(f"New cell phone ({contact['cell_phone']}): ").strip() or contact['cell_phone']
            email = input(f"New email ({contact['email']}): ").strip() or contact['email']

            if not name:
                print("Please enter a valid name")
                return
            if not last_name:
                print("Please enter a valid last name")
                return
            if not telephone or not telephone.isdigit():
                print("Please enter a valid telephone number")
                return
            if not cell_phone or not cell_phone.isdigit():
                print("Please enter a valid cellphone number")
                return
            if email and not "@" in email:
                print("Please enter a valid email address")
                return

            contact["name"] = name
            contact["last_name"] = last_name
            contact["telephone"] = telephone
            contact["cell_phone"] = cell_phone
            contact["email"] = email

            print("Contact updated successfully")
            return

    print("There is no contact with the same id")


def delete_contact(id):
    for contact in address_book:
        if contact['id'] == id:
            address_book.remove(contact)
            print("Contact deleted successfully")
            return

    print("There is no contact with the same id")


def manage_option(option):
    match option:
        case 1:
            view_contacts()
        case 2:
            id = input("Please enter id of the contact: ")
            especific_contact(id)
        case 3:
            add_contact()
        case 4:
            id = input("Please enter id of the contact you want to update: ")
            update_contact(id)
        case 5:
            id = input("Please enter id of the contact you want to delete: ")
            delete_contact(id)
        case 6:
            print(f"Goodbye {user}")
        case _:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    while True:
        print(f"Welcome to your address book {user}")
        print("""Menu
        1. View contacts in your address book
        2. View a specific contact from your address book
        3. Add a new contact to the address book
        4. Update a contact in your address book
        5. Delete a contact in your address book
        6. Exit the address book
        """)
        option = int(input("Please enter your option: "))
        manage_option(option)
        if option == 6:
            break
