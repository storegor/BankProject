def withdraw(self, value):
    exit_code = withdraw(self.id_, self.current_bank_, self.current_account_, value)
    if exit_code == 1:
        print("Вы не можете снять столько денег! Дополните информацию профиля")
    if exit_code == 2:
        print("Ошибка! На счету недостаточно средств")
    if exit_code == 3:
        print("Вы сняли" + " " + f'{value}' + ' ' + "рублей!")
        write_in_history(self.id_, self.current_bank_, self.current_account_, value, 'W')
        data_base.save("Data_Base.xlsx")
    if exit_code == 4:
        print("Вы вышли за кредитный лимит! Дополните информацию профиля")
    if exit_code == 5:
        print("Вы сняли" + " " + f'{value}' + ' ' + "рублей!")
        write_in_history(self.id_, self.current_bank_, self.current_account_, value, 'W')
        data_base.save("Data_Base.xlsx")
    if exit_code == 6:
        print("Ошибка! Депозит еще не истек")
    if exit_code == 7:
        print("Вы сняли" + " " + f'{value}' + ' ' + "рублей!")
        write_in_history(self.id_, self.current_bank_, self.current_account_, value, 'W')
        data_base.save("Data_Base.xlsx")
    if exit_code == 8:
        print("Ошибка! На счету недостаточно средств")

def put(self, value):
    exit_code = put(self.id_, self.current_bank_, self.current_account_, value)
    if exit_code == 1 or exit_code == 2 or exit_code == 3:
        print("Вы положили" + " " + f'{value}' + ' ' + "рублей!")
        write_in_history(self.id_, self.current_bank_, self.current_account_, value, 'P')
        data_base.save("Data_Base.xlsx")

def transfer(self, value, dest_bank, dest_account, dest_id):
    exit_code_w = withdraw(self.id_, self.current_bank_, self.current_account_, value)
    if exit_code_w == 3 or exit_code_w == 5 or exit_code_w == 7:
        exit_code_p = put(dest_id, dest_bank, dest_account, value)
        if exit_code_p == 1 or exit_code_p == 2 or exit_code_p == 3:
            print("Вы перевели" + " " + f'{value}' + ' ' + "рублей!")
            write_in_history(self.id_, self.current_bank_, self.current_account_, value, 'T', dest_id, dest_bank, dest_account)
            data_base.save("Data_Base.xlsx")
    if exit_code_w == 1:
        print("Вы не можете снять столько денег! Дополните информацию профиля")
    if exit_code_w == 2:
        print("Ошибка! На счету недостаточно средств")
    if exit_code_w == 4:
        print("Вы вышли за кредитный лимит! Дополните информацию профиля")
    if exit_code_w == 6:
        print("Ошибка! Депозит еще не истек")
    if exit_code_w == 8:
        print("Ошибка! На счету недостаточно средств")





