from Check import *
from ClientBuilder import ClientBuilder

def ui_sign_up_or_log_in():
    print("Введи пользовательский id, если хотите войти в существующий профиль или 'Новый пользователь', если хотите зарегистрировать новый профиль")
    print("Введите 'Назад', если хотите вернуться на предыдущий экран")
    check_id = input()
    if check_id == 'Назад':
        return user_back_step()
    elif check_id == 'Новый пользователь':
        return ui_new_user()
    else:
        while not :
            print("Пользователь с таким id не найден, повторите попытку или зарегистрируйте нового пользователя (Введите 'Назад')")
            check_id = input()
            if check_id == 'Назад':
                back = True
                break
        else:
            return ui_user_choose_bank()
        if back:
            return ui_sign_up_or_log_in()



def ui_new_user():
    client_bank = check_bank(input('Выберете банк (напишите Сбербанк/ВТБ/Тинькофф)(Обязательное поле): '))
    client_name = check_name(input('Впишите Ваши фамилию и имя (обязательное поле): '))
    client_passport = input('Введите серию и номер паспорта: ')
    client_address = input('Введите Ваш адрес: ')
    builder = ClientBuilder()
    builder.set_id(id_)
    builder.set_name(client_name)
    builder.set_bank(client_bank)
    if client_passport != ' ':
        builder.set_passport(client_passport)
    if client_address != ' ':
        builder.set_address(client_address)
    print(f"Запомните Ваш уникальный токен, \nс помощью него Вы будете заходить в свой аккаунт \n{id_[0]}")


def ui_user_choose_bank(row_choose_bank):
    name = users_sheet[row_choose_bank][2].value
    bank_list = ' '
    for i in range(3, 6):
        if users_sheet[row_choose_bank][i].value == 1:
            bank_list += str(users_sheet[1][i].value) + ' '
    print(f"Добро пожаловать, {name}")
    print(f'Список банков, где вы зарегистрированны: {bank_list}')
    print("Введите название банка, в который хотите войти или 'Зарегистрироваться в новом банке', если хотите открыть счет в другом банке")
    print("Введите 'Назад', если хотите выйти из текущего профиля")
    bank = input()
    if bank == 'Назад':
        return ui_sign_up_or_log_in()
    if bank == 'Зарегистрироваться в новом банке':
        return ui_bank_registration(bank)
    back = False
    while bank_list.find(bank) < 0:
        if bank == 'Назад':
            back = True
            break
        print('Вы не зарегистрированны в этом банке или ввели некоректоное значение, повторите попытку')
        print("Введите 'Назад', если хотите вернуться на предыдущий экран")
        bank = input()
    else:
        return ui_bank_first_screen(bank, row_choose_bank)
    if back:
        return ui_user_choose_bank(row_choose_bank)


def ui_bank_first_screen(bank, row_choose_bank):
    global client
    client.set_bank(bank)
    if bank == 'Сбербанк':
        sheet1 = data_base.worksheets[1]
    if bank == 'ВТБ':
        sheet1 = data_base.worksheets[2]
    if bank == 'Тинькофф':
        sheet1 = data_base.worksheets[3]
    print("Список ваших счетов: ")
    account_list = ' '
    row = search_in_column(int(client.id_), sheet1, 1)
    for i in range(2, 5):
        if sheet1[row][i].value is not None:
            account_list += str(sheet1[1][i].value) + '\n' + ' '
    print('=' * 60)
    print(account_list[:-2])
    print('=' * 60)
    print("Введите 'История операций', чтобы посмотреть историю операций")
    print("Введите название счёта, чтобы перейти на него")
    print("Введите 'Открыть новый счёт', чтобы открыть новый счёт")
    print("Введите 'Назад', если хотите вернуться на предыдущий экран")
    if sheet1[row][7] == 0:
        account = input()
        print("Введите 'Дополнить информацию о профиле', чтобы дополнить информацию о профиле")
        if account == 'Дополнить информацию о профиле':
            return ui_add_info(sheet1, bank, row_choose_bank)
    account = input()
    if account == 'Назад':
        return ui_user_choose_bank(row_choose_bank)
    if account == 'Открыть новый счёт':
        return ui_new_account_registration(bank, row_choose_bank)
    if account == 'История операций':
        return ui_operations_history(bank, row_choose_bank)
    back = False
    while account_list.find(account) < 0:
        if account == 'Назад':
            back = True
            break
        print('У вас нет такого счёта или вы ввели некоректоное значение, повторите попытку')
        print("Введите 'Назад', если хотите вернуться на предыдущий экран")
        account = input()
    else:
        return ui_account_first_screen(bank, row_choose_bank, account)
    if back:
        return ui_bank_first_screen(bank, row_choose_bank)



def ui_account_first_screen(bank, row_choose_bank, account):
    print(3)

def ui_new_account_registration(bank, row_choose_bank):
    print(4)

def ui_bank_registration(bank, row_choose_bank):
    print(2)

def ui_operations_history(bank, row_choose_bank):
    print("История пополнений и снятий:")
    print('_' * 20)
    sheet = excel_file.worksheets[6]
    for i in range(2, sheet.max_row + 5):
        if sheet[i][0].value == client.id_:
            if sheet[i][1].value == client.current_bank_:
                print('Счёт:', sheet[i][2].value)
                print('Операция:', sheet[i][3].value)
                print('Сумма:', sheet[i][4].value)
                print('_' * 20)
    print('=' * 60)                 ########    4600637182
    print("История переводов: ")
    print('_' * 20)
    sheet = excel_file.worksheets[4]
    for i in range(2, sheet.max_row + 5):
        if sheet[i][2].value == int(client.id_):
            if sheet[i][0].value == client.current_bank_:
                print('Счёт:', sheet[i][1].value)
                print('Кому:', find_name_by_id(sheet[i][5].value))
                print('В какой банк:', sheet[i][3].value)
                print('На какой счёт:', sheet[i][4].value)
                print('Сумма:', sheet[i][6].value)
                print('_' * 20)
    print("Введите 'Отменить перевод', если хотите отменить перевод")
    print("Введите 'Назад', если хотите вернуться на предыдущий экран")
    cansel = input()
    if cansel == 'Назад':
        return ui_bank_first_screen(bank, row_choose_bank)
    if cansel == 'Отменить перевод':
        data = []
        data.append(input("Введите счёт списания:\n"))
        data.append(input("Введите получателя(id):\n"))
        data.append(input("Введите банк получателя:\n"))
        data.append(input("Введите счёт получателя:\n"))
        data.append(input("Введите сумму:\n"))
        data.append(int(client.id_))
        data.append(client.current_bank_)
        for i in range(2, sheet.max_row + 5):
            if sheet[i][0].value == data[6]:
                if sheet[i][1].value == data[0]:
                    if sheet[i][2].value == data[5]:
                        if sheet[i][3].value == data[2]:
                            if sheet[i][4].value == data[3]:
                                if sheet[i][5].value == data[1]:
                                    if sheet[i][6].value == data[4]:
                                        sheet[i][7] = input("Введите причину отмены: ")
                                        print("Запрос об отмене будет рассмотрен в течении 30 рабочих дней!")
                                        break
        return ui_operations_history(bank, row_choose_bank)


def ui_add_info(sheet1, bank, row_choose_bank):
    row = search_in_column(client.id_, sheet1, 1)
    sheet1[row][5] = input("Введите свой адрес: \n")
    sheet1[row][6] = input("Введите номер своего паспорта: \n")
    excel_file.save('Data_Base.xlsx')
    print("Данные успешно сохранены!")
    return ui_bank_first_screen(bank, row_choose_bank)

def user_back_step():
    value = check_first_screen(
        input("Введите 'Б' или 'П' для перехода в банковский или пользовательский интерфейс соответственно:\n"))
    if value == 'Б':
        return choose_bank()
    if value == 'П':
        return ui_sign_up_or_log_in()




excel_file.save('Data_Base.xlsx')

from BankInterface import choose_bank

excel_file.save('Data_Base.xlsx')