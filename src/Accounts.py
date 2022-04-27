class IAccount:
    def __init__(self):
        self.amount = None
        self.id = None

    def transfer(self, other_account, value):
        pass

    def withdraw(self, value):
        pass

    def put(self, value):
        pass


class DebitAccount(IAccount):
    def __init__(self):
        super().__init__()

    def transfer(self, other_account, value):
        if self.amount >= value or ...:
            self.amount -= value
            other_account.amount += value

    def put(self, value):
        self.amount += value

    def withdraw(self, value):
        if self.amount >= value or ...:
            self.amount -= value


class CreditAccount(IAccount):
    def __init__(self):
        super().__init__()
        self.commission = None
        self.limit = None


class DepositAccount(IAccount):
    def __init__(self):
        super().__init__()
        self.date_close = None


class IOpenAccount:
    def create(self) -> IAccount:
        pass


class OpenDebit(IOpenAccount):
    def create(self):
        return DebitAccount()


class OpenCredit(IOpenAccount):
    def create(self):
        return CreditAccount()


class OpenDeposit(IOpenAccount):
    def create(self):
        return DepositAccount()
