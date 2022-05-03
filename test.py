from src.ClientBuilder import ClientBuilder
from src.BankBuilder import BankBuilder
from src.Accounts import ForeignAccount, DebitAccount, DepositAccount, OpenDebit, OpenDeposit, OpenForeign, OpenCredit
import unittest


class TestBank(unittest.TestCase):

    def test_client_builder(self):
        client_builder = ClientBuilder()
        bank_builder = BankBuilder()
        debit_account_opener = OpenDebit()
        debit_account = debit_account_opener.create(0, client_builder, bank_builder.bank_, 3000)
        client_builder.set_name('Вася Пупкин')
        client_builder.set_id(2453243214143)
        client_builder.set_current_account(debit_account)
        client_builder.set_current_bank(bank_builder.bank_)
        client_builder.add_account_to_list(debit_account)
        self.assertEqual(client_builder.client.name_, 'Вася Пупкин')
        self.assertEqual(client_builder.client.id_, 2453243214143)
        self.assertEqual(client_builder.client.current_account_, debit_account)
        self.assertEqual(client_builder.client.current_bank_, bank_builder.bank_)
        self.assertEqual(client_builder.client.all_accounts_, [debit_account])
        client_builder.client.current_account_.put(1000)
        self.assertEqual(client_builder.client.current_account_.show_amount(), 1000)
        self.assertRaises(Exception, client_builder.client.current_account_.withdraw, 5000)
        client_builder.client.current_account_.put(5000)
        self.assertEqual(client_builder.client.current_account_.show_amount(), 6000)
        debit_account.bank_ = client_builder.client.current_bank_
        self.assertEqual(debit_account.bank_, bank_builder.bank_)
        bank_builder.add_client_info('el;mlj', 288, client_builder.client)
        bank_builder.set_current_client(client_builder.client)
        bank_builder.add_client(client_builder.client)
        client_builder.client.current_account_.withdraw(3000)
        self.assertEqual(client_builder.client.current_account_.show_amount(), 3000)

