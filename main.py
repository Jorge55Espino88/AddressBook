from datetime import datetime
from addressbook import AddressBook

print("*** Address Book ***")

user = input("Please enter your name: ")
address_book = AddressBook()


def manage_option(option):
    match option:
        case 1:
            address_book.view_contacts()
        case 2:
            contact_id = input("Please enter id of the contact: ").strip()
            address_book.view_especific_contact(contact_id)
        case 3:
                name = input("Please enter the name: ").strip()
                last_name = input("Please enter the last name: ").strip()
                telephone = input("Please enter the telephone number: ").strip()
                cell_phone = input("Please enter the cell phone: ").strip()
                email = input("Please enter the email: ").strip()
                address_book.add_contact(name, last_name, telephone, cell_phone, email)

        case 4:
            contact_id = input("Please enter id of the contact you want to update: ").strip()
            if not contact_id:
                print("ID cannot be empty")
                return

            current_contact = None
            for contact in address_book.contacts:
                if contact.id == contact_id:
                    current_contact = contact
                    break

            if not current_contact:
                print("Contact not found")
                return


            name = input(f"New name ({current_contact.name}): ").strip() or current_contact.name
            last_name = input(f"New last name ({current_contact.last_name}): ").strip() or current_contact.last_name
            telephone = input(f"New telephone ({current_contact.telephone}): ").strip() or current_contact.telephone
            cell_phone = input(f"New cell phone ({current_contact.cell_phone}): ").strip() or current_contact.cell_phone
            email = input(f"New email ({current_contact.email}): ").strip() or current_contact.email

            address_book.edit_contact(
                contact_id,
                name=name if name != current_contact.name else None,
                last_name=last_name if last_name != current_contact.last_name else None,
                telephone=telephone if telephone != current_contact.telephone else None,
                cell_phone=cell_phone if cell_phone != current_contact.cell_phone else None,
                email=email if email != current_contact.email else None
            )
        case 5:
            contact_id = input("Please enter id of the contact you want to delete: ").strip()
            address_book.delete_contact(contact_id)
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
        try:
            option = int(input("Please enter your option: "))
            manage_option(option)
            if option == 6:
                break
        except ValueError:
            print("Invalid option. Please try again.")
