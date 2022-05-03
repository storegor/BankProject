from src.ClassBank import Bank


class BankBuilder:

    def __init__(self):
        self.bank_ = Bank()

    def set_name(self, name):
        self.bank_.name_ = name

    def add_client(self, client):
        self.bank_.all_clients_.append(client)

    def set_current_client(self, client):
        self.bank_.current_client_ = client

    def set_current_account(self, account):
        self.bank_.current_account_ = account

    def add_account(self, account):
        self.bank_.accounts_.append(account)

    def add_client_info(self, address, passport, client):
        self.bank_.client_info.update({client: [passport, address]})

    def write_cansel_message(self, message):
        self.bank_.cansel_message = message
