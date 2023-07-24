

def add_contact(*args):
    name = Name(args[0])
    if len(args) == 2:

        # name = Name(args[0])
        phone = Phone(args[1])
        rec: Record = address_book.get(str(name))
        if rec:
            return rec.add_phone(phone)
        rec = Record(name, phone, birthday)
    if len(args) > 2:
        try:
            if datetime.datetime.strptime(args[2], "%d.%m.%Y"):
                birthday = Birthday(args[2])
                print(birthday)
        except ValueError:
            print('Invalid date!')
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
