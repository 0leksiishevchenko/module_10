from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    
class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(self.validate_phone(value))

    @staticmethod
    def validate_phone(phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid phone number format. Please enter a 10-digit number.")
        return phone

    
class Record:
    
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        drop_contact = self.find_phone(phone)
        if drop_contact:
            self.phones.remove(drop_contact)

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError(f"Phone {old_phone} not found in the record.")

    def find_phone(self, phone):
        try:
            for contact in self.phones:
                if contact.value == phone:
                    return contact

            raise ValueError(f"Phone {phone} not found in the record.")
        except ValueError:
            pass #print(f"Phone {phone} not found in the record.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(contact.value for contact in self.phones)}"

    
class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        try:
            if name in self.data:
                del self.data[name]
            else:
                raise KeyError(f"Record with name {name} not found in the address book.")
        except KeyError:
            pass #print(f"Record with name {name} not found in the address book.")
        

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")