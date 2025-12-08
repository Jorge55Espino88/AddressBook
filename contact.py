from datetime import datetime


class Contact:
    contact_id = 0

    def __init__(self, name,last_name,telephone, cell_phone, email):
        Contact.contact_id += 1
        date = datetime.now().date()
        self.__id = f"{date.year}{date.month:02d}{date.day:02d}-{Contact.contact_id}"
        self.name = name
        self.last_name = last_name
        self.telephone = telephone
        self.cell_phone = cell_phone
        self.email = email

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, value):
        value = value.strip()
        if not value:
            raise ValueError("Last name cannot be empty")
        self.__last_name = value

    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self, value):
        value = value.strip()
        if not value or not value.isdigit():
            raise ValueError("Telephone number must be numeric and cannot be empty")
        self.__telephone = value

    @property
    def cell_phone(self):
        return self.__cell_phone
    @cell_phone.setter
    def cell_phone(self, value):
        value = value.strip()
        if not value or not value.isdigit():
            raise ValueError("Cell phone number must be numeric and cannot be empty")
        self.__cell_phone = value

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        value = value.strip()
        if value and not "@" in value:
            raise ValueError("Insert a valid email address")
        self.__email = value


    def __str__(self):
        return f"""
        Id: {self.__id}
        Name: {self.__name}
        Last name: {self.__last_name}
        Telephone: {self.__telephone}
        Cell phone: {self.__cell_phone}
        Email: {self.__email}
        """


if __name__ == '__main__':
    try:
        contact1 = Contact("Jorge","Espino","mm","56656656","correo@correo.com")

        print(contact1)
        print(contact1.id)
        print(contact1.name)
        print(contact1.last_name)
        print(contact1.telephone)
        print(contact1.cell_phone)
        print(contact1.email)

        contact1.telephone = "3344455555"
        print(contact1.telephone)
    except ValueError as error:
        print(error)