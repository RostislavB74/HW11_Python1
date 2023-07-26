
import datetime
from datetime import datetime
from ab_classes_240723_w import AddressBook, Name, Phone, Record, Birthday
import re

address_book = AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NameError as e:
            print(
                f"Give me a name and  phone number in format +380(88)777-77-77")
        except IndexError as e:
            print(
                f"Give me a name and  phone number in format +380(88)777-77-77")
        except TypeError as e:
            print(
                f"Give me a name and  phone number in format +380(88)777-77-77")
        except UnboundLocalError as e:
            print("Contact exists")
        except ValueError as e:
            print(
                f"Give me a name and  phone number in format +380(88)777-77-77")
        except AttributeError as e:
            print(
                f"Give me a name and  phone number in format +380(88)777-77-77")
    return wrapper


# @input_error
def add_contact(*args):
    name = Name(args[0])
    rec: Record = address_book.get(str(name))
    # if rec:

    #     return rec.add_phone(phone)
    if len(args) == 2:
        pattern_bd = r'(\d\d)/(\d\d)/(\d{4})'
        if re.fullmatch(pattern_bd, args[1]):
            #        rec: Record = address_book.get(str(name))
            data = Birthday(args[1])
        # print(data.value)
            if isinstance(data.value, datetime):
                birthday = data
                #  print(birthday)
                if rec:
                    birthday = data
                    return rec.add_birthday(birthday)
                rec = Record(name, birthday=birthday)
        else:
            phone = Phone(args[1])
            # birthday = None
            # rec = Record(name, phone)
            if rec:
                return rec.add_phone(phone)
            rec = Record(name, phone=phone)
#             return address_book.add_record(rec)
        # print('Invalid date!')
        # print(type(args[1]))

        return address_book.add_record(rec)
    if len(args) > 2:
        # name = Name(args[0])
        list_phones = []
        rec: Record = address_book.get(str(name))
        if rec:
            for i in range(1, len(args)):
                list_phones.append(Phone(args[i]))
            # return rec.add_phone(list_phones)
        else:
            for i in range(1, len(args)):
                list_phones.append(Phone(args[i]))
            rec = Record(name, list_phones)

        return address_book.add_record(rec)
    else:
        return "Unknown command"
# def add_contact(*args):
#     name = Name(args[0])
#     rec: Record = address_book.get(str(name))

#     for i in range(1, len(args)):
#         print(args[i])

#         if Birthday(args[i]):
#             birthday = Birthday(args[i])
#         # if isinstance(birthday, datetime):
#         # print(birthday.value)

#             if rec:
#                 # birthday = data
#                 return rec.add_birthday(birthday)
#             rec = Record(name, birthday=birthday)
#             return address_book.add_record(rec)
#         if Phone(args[i]):
#             phone = Phone(args[i])
#         # birthday = None
#         # rec = Record(name, phone)
#             if rec:
#                 return rec.add_phone(phone)
#             rec = Record(name, phone=phone)
#             return address_book.add_record(rec)
#     # print('Invalid date!')
#     # print(type(args[1]))
#         else:
#             return "Unknown command"

# if len(args) > 2:
    #     # name = Name(args[0])
    #     list_phones = []
    #     rec: Record = address_book.get(str(name))
    #     if rec:
    #         for i in range(1, len(args)):
    #             list_phones.append(Phone(args[i]))
    #         return rec.add_phone(list_phones)
    #     else:
    #         for i in range(1, len(args)):
    #             list_phones.append(Phone(args[i]))
    #         rec = Record(name, list_phones)

    #         return address_book.add_record(rec)

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


def get_days_to_birthday(*args):
    name = Name(args[0])
    # result = main_bd(address_book.get((Birthday(name))))
    res: Record = address_book.get(str(name))
    return res.days_to_birthday(res.birthday)
    # return f"User {address_book.get(str(name))}"


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
    add_contact: ("add ", "+ ", "1"),
    change_phone: ("change ", "зміни ", "2"),
    remove_phone: ("remove ", "delete ", "del ", "-", "3"),
    exit_command: ("good bye", "bye", "exit", "end", "close", "quit", "0"),
    show_all_command: ("show all", "show", "4"),
    hello: ("hello", "hi", "!"),
    get_days_to_birthday: ("birthday", "bd", "6"),
    get_phone: ("phone ", "5",)

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
        # print(address_book.data.keys())
        # print(address_book.data.values(Birthday()))
        # with open('names.csv', 'w', newline='') as fh:
        #     writer = csv.DictWriter(fh, fieldnames=list(address_book.data(Record())), quoting=csv.QUOTE_NONNUMERIC)
        #     writer.writeheader()
        #     for d in address_book:
        #         writer.writerow(d)

        # with open('contact.txt', 'a') as f:

        # print(address_book)
        #   f.writelines([data for data in address_book])
        user_input = input(">>>")
        cmd, data = parser(user_input)
        result = cmd(*data)
        print(result)
        #
        if cmd == exit_command:
            break


if __name__ == "__main__":
    main()
