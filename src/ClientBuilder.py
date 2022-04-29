from ClassClient import Client
from random import randint


def create_id(admin):
    client_id = randint(10 ** 9, 10 ** 10 - 1)
    while client_id in admin.all_clients_id_:
        client_id = randint(10 ** 9, 10 ** 10 - 1)
    admin.all_clients_id_.append(client_id)
    return client_id


class ClientBuilder:
    def __init__(self):
        self.client = Client()

    def set_name(self, name):
        self.client.name_ = name

    def set_id(self, admin):
        self.client.id_ = create_id(admin)

    def set_current_account(self, account):
        self.client.current_account_ = account

    def set_current_bank(self, bank):
        self.client.current_bank_ = bank

    def add_account_to_list(self, account):
        self.client.all_accounts_.append(account)

