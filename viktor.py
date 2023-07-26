address_boor = {}


def error_with_func(arg1, arg2):
    def input_error(func):
        def proc_error(*args):
            print(args)
            try:
                return func(*args)
            except (IndexError, ValueError):
                return f'Добавьте все данные корректно в команду \033[34m{arg1}\033[0m по шаблону: \033[34m<{arg2}>\033[0m'
            except KeyError:
                return f'Нет такого {args[0]} контакта в вашей книге'
        return proc_error
    return input_error


@error_with_func('phone', 'phone [name]')
def add(*args):
    raise KeyError()
    # print(args[0])


if __name__ == "__main__":
    print(add("Bill"))
