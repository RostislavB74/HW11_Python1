from ex111 import Car, Garage

garage = Garage()


def show_command(*args):
    return garage


def exit_command(*args):
    return "Bye bye"


def add_command(*args):
    car = Car(args[0])
    garage.add_car(car)
    return "Car added"


def main():
    while True:
        user_input = input(">>>")
        if user_input.startswith("show all"):
            result = show_command()
        elif user_input.startswith("add"):
            result = add_command(user_input[len("add"):].strip())
        elif user_input.startswith("exit"):
            print(exit_command())
            break
        elif user_input.startswith("pages"):
            rec_per_page = None
            try:
                rec_per_page = int(user_input[len("pages"):].strip())
            except ValueError:
                rec_per_page = 3
            for car in garage.iterator(rec_per_page):
                print(car)
                input("For next page press any key")
        print(result)


if __name__ == "__main__":
    main()
