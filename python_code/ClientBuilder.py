from ClassClient import Client


class ClientBuilder:
    def __init__(self):
        self.client = Client()

    def set_name(self, name_):
        self.client.name = name_

    def set_id(self, id_):
        self.client.id = id_

    def set_account(self, account_):
        self.client.current_account = account_

    def set_passport(self, passport_):
        self.client.passport = passport_

    def set_address(self, address_):
        self.client.address = address_

    def set_all_accounts(self, account, value):
        self.client.all_accounts[account] = value

