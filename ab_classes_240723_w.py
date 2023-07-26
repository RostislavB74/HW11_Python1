from collections import UserDict
import time
import re
from bd import main_bd
from datetime import datetime
from collections import UserDict


class Field:

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)


class Name(Field):
    ...


class Phone(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value
        # print(self.value)

    @property
    def value(self):
        return self.__value.group()

    @value.setter
    def value(self, value):
        pattern = r"(\+\d{3}\(\d{2}\)\d{3}\-(?:(?:\d{2}\-\d{2})|(?:\d{1}\-\d{3}){1}))"
        try:
            self.__value = re.match(pattern, value)
            # matches = self.__value.finditer(sentence)
            # for match in matches:
            # print(self.__value.group())

        except ValueError:
            return

    def __str__(self):
        return self.__value.group()


class BirthdayError(Exception):
    ...


class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value
        # print(self.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            if datetime.strptime(value, "%d/%m/%Y"):
                self.__value = datetime.strptime(value, "%d/%m/%Y")
        except ValueError:
            return value

    def __str__(self):
        return self.__value.strftime("%d/%m/%Y")


class Email(Field):
    ...


class Record:

    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None) -> None:
        self.name = name
        self.phones = []
        self.birthday = birthday
        # if birthday:
       #    self.birthdays.append(birthday)
        if phone:
            if isinstance(phone, list):
                self.phones.extend(phone)
            else:
                self.phones.append(phone)

    def add_birthday(self, birthday: Birthday):
        # print(birthday)
        # print(self.birthday)
        if birthday:
            self.birthdays = birthday
            return f"birthday {birthday} add to contact {self.name}"
        return f"{birthday} present in birthday data of contact {self.name}"

    def add_phone(self, phone: Phone):
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

    def days_to_birthday(self, birthday: Birthday):
        # print(birthday)
        result = main_bd(birthday)
        return result

    def __str__(self) -> str:
        # if self.birthday:
        #    return f"{self.name}: "
        # if self.phones:
        return f"{self.name}: {', '.join(str(p) for p in self.phones)}, {(str(self.birthday))}"
#    def __str__(self) -> str:

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
        # print(record)
        self.data[str(record.name)] = record
        return f"Contact {record} add success"
    # def add_record1(self, record: Record):
    #     self.data[str(record.name)] = record
    #     return f"Contact {record} add success"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
