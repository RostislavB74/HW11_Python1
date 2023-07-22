from collections import UserDict
import time


class Field:

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)


class Birthday(Field):
    ...


class Name(Field):
    ...


class Phone(Field):
    ...


class Email(Field):
    ...


class Record:

    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None, email: Email = None) -> None:
        self.name = name
        self.phones = []
        self.birthday = birthday
        self.email = email
        if phone:
            if isinstance(phone, list):
                self.phones.extend(phone)
            else:
                self.phones.append(phone)

    def add_birthday(self, birthday: Birthday):
        if isinstance(birthday, time):
            self.birthday = birthday
        return self.birthday

    def add_phone(self, phone: Phone):
        if isinstance(phone, list):
            for i in range(len(phone)):
                if phone[i] not in [p for p in self.phones]:
                    self.phones.extend(phone)

            return f"The contact {self.name} was updated"
        else:
            if phone.value not in [p.value for p in self.phones]:
                self.phones.append(phone)
                return f"phone {phone} add to contact {self.name}"
        return f"{phone} present in phones of contact {self.name}"

    def change_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[idx] = new_phone
                return f"old phone {old_phone} change to {new_phone}"
        return f"{old_phone} not present in phones of contact {self.name}"

    def days_to_birthday():
        pass

    def __str__(self) -> str:
        return f"{self.name}: {', '.join(str(p) for p in self.phones)}"

    def remove_phone(self, phone):
        for idx, p in enumerate(self.phones):
            if phone.value == p.value:
                # print(self.phones)
                old_phone = (self.phones[idx])
                self.phones.remove(self.phones[idx])
                return f"The phone {old_phone} is deleted"
        return f"{phone} not present in phones of contact {self.name}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} add success"
    # def add_record1(self, record: Record):
    #     self.data[str(record.name)] = record
    #     return f"Contact {record} add success"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
