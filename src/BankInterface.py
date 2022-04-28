from Check import *
from ClassClient import *

excel_file = openpyxl.open('Data_Base.xlsx', read_only=False, data_only=True)
users_sheet = excel_file['Пользователи']


def choose_operation(bank):
    decision = input("Выберете что Вы хотитие узнать(Уведомления, Список клиентов)(Если хотите вернуться к выбору банка, введите Назад): ")
    while decision != "Уведомления" and decision != "Статистика" and decision != 'Назад':
        print("Введенная строка некорректна, попробуйте снова")
        decision = input("Выберете, что Вы хотитие узнать(Уведомления, Список клиентов)(Если хотите вернуться к выбору банка, введите Назад): ")
    if decision == "Список клиентов":
        print('=' * 60)
        clients_list(bank)
        print('=' * 60)
        movement = input("Вывести имеющиеся счета клиента?(Да, Нет): ")
        while movement != "Нет" and movement != "Да":
                print("Введенная строка некорректна, попробуйте снова")
                movement = input("Вывести имеющиеся счета клиента?(Да, Нет): ")
        if movement == "Да":
            client_id = int(input("Введите Id клиента, чьи счета хотите вывести: "))
            client_row = search_in_column(client_id, excel_file[bank], 1)
            while client_row == False:
                client_id = input("Введенный Id не существует, попробуйте снова: ")
                client_row = search_in_column(client_id, excel_file[bank], 1)
            print('*' * 60)
            print('Дебетовый счет(₽)/Депозит(₽)/Кредитный счёт(₽)')
            print(0 if get_cell(excel_file[bank], client_row, 2) is None else get_cell(excel_file[bank], client_row, 2),
                  0 if get_cell(excel_file[bank], client_row, 3) is None else get_cell(excel_file[bank], client_row, 3),
                  0 if get_cell(excel_file[bank], client_row, 4) is None else get_cell(excel_file[bank], client_row, 4), sep='/')
            print('*' * 60)
            choose_operation(bank)
        elif movement == "Нет":
            choose_operation(bank)
    elif decision == "Уведомления":
        print('--' * 30)
        for i in range(2, excel_file['История переводов'].max_column + 1):
            if get_cell(excel_file['История переводов'], i, 7) != None:
                print(f"Текст уведомления:\n{get_cell(excel_file['История переводов'], i, 7)}")
                print(f"Инофрмация о переводе:\nFrom: {get_cell(excel_file['История переводов'], i, 0)}"
                      f"/{get_cell(excel_file['История переводов'], i, 1)}/"
                      f"{get_cell(excel_file['История переводов'], i, 2)}\nTo: "
                      f"{get_cell(excel_file['История переводов'], i, 3)}/"
                      f"{get_cell(excel_file['История переводов'], i, 4)}/"
                      f"{get_cell(excel_file['История переводов'], i, 5)}\nAmount: "
                      f"{get_cell(excel_file['История переводов'], i, 6)}")
                print('--' * 30)
                manager_decision = input("Отменить перевод?(Да, Нет): ")
                while manager_decision != "Да" and manager_decision != "Нет":
                    print("Введенная строка некорректна, попробуйте снова")
                    manager_decision = input("Отменить перевод?(Да, Нет): ")
                if manager_decision == "Да":
                    set_cell(excel_file['История переводов'], i, 7, None)
                    excel_file.save('Data_Base.xlsx')
                    recipient = Client(get_cell(excel_file['История переводов'], i, 5))
                    recipient.current_bank_ = get_cell(excel_file['История переводов'], i, 3)
                    recipient.current_account_ = get_cell(excel_file['История переводов'], i, 4)
                    recipient.transfer(get_cell(excel_file['История переводов'], i, 6), get_cell(excel_file['История переводов'], i, 0),
                                       get_cell(excel_file['История переводов'], i, 1,), get_cell(excel_file['История переводов'], i, 2))

    elif decision == "Назад":
        choose_bank()


def clients_list(bank):
    bank_sheet = excel_file[bank]
    print("ID/Фамилия Имя/Адрес/Паспорт/Надежность")
    for i in range(2, bank_sheet.max_column + 1):
        necessary_row = search_in_column(get_cell(bank_sheet, i, 1), users_sheet, 1)
        if get_cell(bank_sheet, i, 1) != None:
            print(get_cell(bank_sheet, i, 1), get_cell(users_sheet, necessary_row, 2),
                  get_cell(bank_sheet, i, 5), get_cell(bank_sheet, i, 6),
                  "Надежный" if get_cell(bank_sheet, i, 7) else "Ненадежный",
                  sep='/')  # id + name + address + pasport + relyable?


def choose_bank():
    print("Введите название банка, в который хотите войти:'Сбербанк', 'ВТБ', 'Тинькофф'")
    print("Введите 'Назад', если хотите вернуться к выбору интерфейса")
    Bank = input()
    if Bank == 'Назад':
        return bank_back_step()
    elif Bank == 'Сбербанк':
        print("Вы вошли в Сбербанк")
        choose_operation(Bank)
    elif Bank == 'ВТБ':
        print('Вы вошли в ВТБ')
        choose_operation(Bank)
    elif Bank == "Тинькофф":
        print("Вы вошли в Тинькофф")
        choose_operation(Bank)

def bank_back_step():
    if input("Введите 'Б' или 'П' для перехода в банковский или пользовательский интерфейс соответственно\n") == 'Б':
        return choose_bank()
    else:
        return ui_sign_up_or_log_in()


excel_file.save('Data_Base.xlsx')
from UserInterface import ui_sign_up_or_log_in

excel_file.save('Data_Base.xlsx')
