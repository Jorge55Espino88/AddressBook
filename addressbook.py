from contact import Contact


class AddressBook:
    def __init__(self):
        self.contacts = []

    def view_contacts(self):
        if self.contacts:
            print("*** View contacts ***")
            for contact in self.contacts:
                print(f"""Id: {contact.id}
                Name: {contact.name}
                Last name: {contact.last_name}
                Telephone: {contact.telephone}
                Cell phone: {contact.cell_phone}
                Email: {contact.email}
        """)
            return
        print(f"No contacts found")

    def view_especific_contact(self, contact_id):
        for contact in self.contacts:
            if contact.id == contact_id:
                print(f"""Id: {contact.id}
                Name: {contact.name}
                Last name: {contact.last_name}
                Telephone: {contact.telephone}
                Cell phone: {contact.cell_phone}
                Email: {contact.email}
                """)
                return
        print(f"No contact found")

    def add_contact(self, name, last_name, telephone, cell_phone, email):
        try:
            contact = Contact(name, last_name, telephone, cell_phone, email)
            self.contacts.append(contact)
            print("New contact added successfully")
        except ValueError as e:
            print(f"Error: {e}")

    def edit_contact(self, contact_id, name = None, last_name = None, telephone = None, cell_phone = None, email = None):
        for contact in self.contacts:
            if contact.id == contact_id:
                try:
                    if name is not None:
                        contact.name = name
                    if last_name is not None:
                        contact.last_name = last_name
                    if telephone is not None:
                        contact.telephone = telephone
                    if cell_phone is not None:
                        contact.cell_phone = cell_phone
                    if email is not None:
                        contact.email = email
                    print("Contact edited successfully")
                    return
                except ValueError as e:
                    print(f"Error: {e}")
                    return

        print("Contact not found")

    def delete_contact(self, contact_id):
        for contact in self.contacts:
            if contact.id == contact_id:
                self.contacts.remove(contact)
                print("Contact deleted successfully")
                return

        print("Contact not found")


if __name__ == '__main__':
    addressbook = AddressBook()
    addressbook.add_contact("Jorge", "Espino", "rrrr","5555", "correo@correo.com")

    print(addressbook.contacts)