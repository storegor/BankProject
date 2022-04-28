from src.ClientBuilder import ClientBuilder
from src.BankBuilder import BankBuilder
from src.Accounts import ForeignAccount, DebitAccount, DepositAccount, OpenDebit, OpenDeposit, OpenForeign, OpenCredit
import unittest


class TestBank(unittest.TestCase):

    def test_client_builder(self):
        client_builder = ClientBuilder()
        bank_builder = BankBuilder()
        debit_account = DebitAccount(0, client_builder, bank_builder, 3000)
        client_builder.set_name('Вася Пупкин')
        client_builder.set_id(2453243214143)
        client_builder.set_current_account(debit_account)
        client_builder.set_current_bank(bank_builder)
        client_builder.add_account_to_list(debit_account)
        self.assertEqual(client_builder.client.name_, 'Вася Пупкин')
        self.assertEqual(client_builder.client.id_, 2453243214143)
        self.assertEqual(client_builder.client.current_account_, debit_account)
        self.assertEqual(client_builder.client.current_bank_, bank_builder)
        self.assertEqual(client_builder.client.all_accounts_, [debit_account])


