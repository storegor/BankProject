import datetime
from AddToTable import *


def withdraw(id_arg, bank, account, value):
    if  < value:
        return 1  ## превышена сумма снятия
    if account == 'Дебетовый счёт':
        if sheet1[row][2].value - value < 0:
            return 2  ## на счету недостаточно средств
        sheet1[row][2].value -= value
        return 3  ## успешно сняли с дебета
    if account == 'Кредитный счёт':
        if sheet1[row][4].value - value < -sheet1[row][8].value:
            return 4  ## выход за кредитный лимит
        sheet1[row][4].value -= value
        return 5  ## успешно сняли с кредитного
    if account == 'Депозит':
        sheet2 = data_base.worksheets[5]
        for i in range(2, sheet2.max_column + 5):
            if sheet2[i][0].value == id_arg:
                deposit_row = i
        year = str(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        if (year + '-' + str(month // 10) + str(month % 10) + '-' + day) <= str(sheet2[deposit_row][4].value)[0:10]:
            return 6   ##депозит еще не истек
        if sheet1[row][3].value - value < 0:
            return 8  ## на счету недостаточно средств
        sheet1[row][3].value -= value
        return 7  ## успешно сняли с депозита


def put(id_arg, bank, account, value):
    if bank == 'Сбербанк':
        sheet1 = data_base.worksheets[1]
    if bank == 'ВТБ':
        sheet1 = data_base.worksheets[2]
    if bank == 'Тинькофф':
        sheet1 = data_base.worksheets[3]
    for i in range(2, sheet1.max_column + 5):
        if sheet1[i][1].value == id_arg:
            row = i
    if account == 'Дебетовый счёт':
        if sheet1[row][2].value is None:
            sheet1[row][2].value = value
        else:
            sheet1[row][2].value += value
        return 1  ## успешно положили на дебет
    if account == 'Кредитный счёт':
        if sheet1[row][4].value is None:
            sheet1[row][4].value = value
        else:
            sheet1[row][4].value += value
        return 2  ## успешно положили на кредитный
    if account == 'Депозит':
        if sheet1[row][3].value is None:
            sheet1[row][3].value = value
        else:
            sheet1[row][3].value += value
        return 3  ## успешно положили на депозит


def write_in_history(id_arg, bank, account, value, operation, id_to=0, bank_to=' ', account_to=' '):
    if operation == 'W' or operation == 'P':
        sheet_withdraw_put = data_base.worksheets[6]
        for i in range(2, sheet_withdraw_put.max_column + 5):
            if sheet_withdraw_put[i][0].value is None:
                row = i
                break
        set_cell(sheet_withdraw_put, row, 0, id_arg)
        set_cell(sheet_withdraw_put, row, 1, bank)
        set_cell(sheet_withdraw_put, row, 2, account)
        set_cell(sheet_withdraw_put, row, 4, value)
        if operation == 'W':
            set_cell(sheet_withdraw_put, row, 3, 'Снятие')
        if operation == 'P':
            set_cell(sheet_withdraw_put, row, 3, 'Пополнение')
    if operation == 'T':
        sheet_transfer = data_base.worksheets[4]
        for i in range(2, sheet_transfer.max_column + 5):
            if sheet_transfer[i][0].value is None:
                row = i
                break
        set_cell(sheet_transfer, row, 0, bank)
        set_cell(sheet_transfer, row, 1, account)
        set_cell(sheet_transfer, row, 2, id_arg)
        set_cell(sheet_transfer, row, 3, bank_to)
        set_cell(sheet_transfer, row, 4, account_to)
        set_cell(sheet_transfer, row, 5, id_to)
        set_cell(sheet_transfer, row, 6, value)
