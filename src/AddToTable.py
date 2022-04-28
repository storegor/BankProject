import random


def set_info(file, client_bank, client_name, client_passport, client_address, client_id):
    users_sheet = file["Пользователи"]
    all_id = []
    client_id.append(random.randint(10 ** 9, 10 ** 10 - 1))
    for i in range(2, users_sheet.max_row + 1):
        if get_cell(users_sheet, i, 1) is not None:
            all_id.append(get_cell(users_sheet, i, 1))
    while client_id[0] in all_id:
        client_id[0] = random.randint(10 ** 9, 10 ** 10 - 1)
    else:
        all_id.append(client_id[0])
        set_cell(users_sheet, len(all_id) + 1, 1, client_id[0]) # id
        set_cell(users_sheet, len(all_id) + 1, 0, len(all_id)) # №
        set_cell(users_sheet, len(all_id) + 1, 2, client_name) # name
        if client_bank == get_cell(users_sheet, 1, 3): #SBer
            users_sheet[len(all_id) + 1][3].value = 1
            set_bank(file["Сбербанк"], client_id, client_address, client_passport)
        elif client_bank == get_cell(users_sheet, 1, 4): #VTB
            users_sheet[len(all_id) + 1][4].value = 1
            set_bank(file["ВТБ"], client_id, client_address, client_passport)
        elif client_bank == get_cell(users_sheet, 1, 5): #Tinkoff
            users_sheet[len(all_id) + 1][5].value = 1
            set_bank(file["Тинькофф"], client_id, client_address, client_passport)
    file.save('Data_Base.xlsx')

def set_bank(sheet, client_id, client_address, client_passport):
    num_of_id = []
    for i in range(2, sheet.max_row + 1):
        if get_cell(sheet, i, 1) is not None:
            num_of_id.append(get_cell(sheet, i, 1))
    set_cell(sheet, len(num_of_id) + 2, 0, len(num_of_id) + 1)
    set_cell(sheet, len(num_of_id) + 2, 1, client_id[0])
    set_cell(sheet, len(num_of_id) + 2, 5, client_address)
    set_cell(sheet, len(num_of_id) + 2, 6, client_passport)