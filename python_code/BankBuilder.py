from ClassBank import Bank


class BankBuilder:

    def __init__(self):
        self.bank_ = Bank()

    def set_name(self, name):
        self.bank_.name_ = name

    def set_users(self, users):
        self.bank_.users_ = users

    def set_current_client(self, client):
        self.bank_.current_client_ = client

    def set_current_account(self, account):
        self.bank_.current_account_ = account

    def add_account(self, account):
        self.bank_.accounts_.append(account)

    def add_client_info(self, adress, passport, client):
        self.bank_.client_info.update({client: [passport, adress]})
