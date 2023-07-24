import time
import datetime
from datetime import datetime
from ab_classes_240723_w import AddressBook, Name, Phone, Record

address_book = AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError as e:
            print(
                f"Give me a name one phone number")
        except TypeError as e:
            print(
                f"Give me a name one phone number")
        except UnboundLocalError:
            print("Contact exists, you can add one number per step")
        except ValueError as e:
            print(
                f"Give me a name one phone number")
        except AttributeError as e:
            print(
                f"Give me a name one phone number")
    return wrapper


@input_error
def add_contact(*args):
    name = Name(args[0])
    if len(args) == 2:
        try:
            birthday = time.strptime(args[1], '%m/%d/%Y')

        except ValueError:

            # name = Name(args[0])
            phone = Phone(args[1])
            rec: Record = address_book.get(str(name))
        if rec:
            return rec.add_phone(phone)
        rec = Record(name, phone)
        return address_book.add_record(rec)
    if len(args) > 2:
        # name = Name(args[0])
        list_phones = []
        rec: Record = address_book.get(str(name))
        if rec:
            for i in range(1, len(args)):
                list_phones.append(Phone(args[i]))
            return rec.add_phone(list_phones)
        else:
            for i in range(1, len(args)):
                list_phones.append(Phone(args[i]))
            rec = Record(name, list_phones)

            return address_book.add_record(rec)
    else:
        return "Unknown command"

# змінити


@input_error
def change_phone(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec: Record = address_book.get(str(name))
    # print(rec)
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"No contact {name} in address book"


# Вийти
def exit_command(*args):
    return "Good bye!"


# показати контакт
@input_error
def get_phone(*args):
    name = Name(args[0])
    # return f"User {name.value}"
    return f"User {address_book.get(str(name))}"


# Привіт
def hello(*args):
    return "How can I help you?"


# Невідома команда пуста команда
def no_command(*args, **kwargs):
    return "Unknown command"


# показати все
def show_all_command(*args):
    return address_book


def days_to_birthday(*args):
    name = Name(args[0])
    return f"User {address_book.get(str(name))}"


# Видалити
@input_error
def remove_phone(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec: Record = address_book.get(str(name))
    # print(rec)
    if rec:
        return rec.remove_phone(phone)
    return f"No contact {name} in address book"


# Команди додати, змінити, видалити, вихід, показати все, показати контакт
COMMANDS = {
    add_contact: ("add ", "+ "),
    change_phone: ("change ", "зміни "),
    remove_phone: ("remove ", "delete ", "del ",),
    exit_command: ("good bye", "bye", "exit", "end", "close", "quit"),
    show_all_command: ("show all", "show"),
    hello: ("hello", "hi"),
    days_to_birthday: ("birthday", "bd"),
    get_phone: ("phone ",)

}


def parser(text: str):
    for cmd, kwds in COMMANDS.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                data = text[len(kwd):].strip().split()
                return cmd, data
    return no_command, []


def main():
    while True:
        user_input = input(">>>")
        cmd, data = parser(user_input)
        result = cmd(*data)
        print(result)
        if cmd == exit_command:
            break


if __name__ == "__main__":
    main()
