from UserInterface import *
import openpyxl
from Check import *
from BankInterface import choose_bank
from UserInterface import ui_sign_up_or_log_in


print("Добро пожаловать в банковскую систему версии 0.1!")
if __name__ == "__main__":
    if input("Введите 'Б' или 'П' для перехода в банковский или пользовательский интерфейс соответственно\n") == 'Б':
        choose_bank()
    else:
        ui_sign_up_or_log_in()

print("Done")
