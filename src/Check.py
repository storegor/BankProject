def check_bank(bank):
    while (bank != "ВТБ" and bank != "Сбербанк" and bank != "Тинькофф"):
        print("Поле пусто или введенные данны некорректы: ")
        bank = input('Выберете банк (напишите Сбербанк/ВТБ/Тинькофф)(Обязательное поле): ')
    return bank

def check_name(name):
    while name == "":
        print("Введеное поле пусто")
        name = input('Впишите Ваши фамилию и имя (обязательное поле): ')
    return name


def check_first_screen(value):
    while value != 'П' and value != 'Б':
        value = input('Вы ввели некоректное значение, повторите попытку:\n')
    return value
