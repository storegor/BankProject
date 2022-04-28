from src.ClassClient import Client


class ClientBuilder:
    def __init__(self):
        self.client = Client()

    def set_name(self, name):
        self.client.name_ = name

    def set_id(self, id_arg):
        self.client.id_ = id_arg

    def set_current_account(self, account):
        self.client.current_account_ = account

    def set_current_bank(self, bank):
        self.client.current_bank_ = bank

    def add_account_to_list(self, account):
        self.client.all_accounts_.append(account)

