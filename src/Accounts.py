from datetime import *

class IAccount:
    def __init__(self, amount, client, bank):
        self.amount_ = amount
        self.client_ = client
        self.bank_ = bank

    def transfer(self, other_account, value):
        raise NotImplementedError

    def withdraw(self, value):
        raise NotImplementedError

    def put(self, value):
        raise NotImplementedError


class DebitAccount(IAccount):
    def __init__(self, amount, client, bank):
        super().__init__(amount, client, bank)

    def transfer(self, other_account, value):
        if self.amount_ >= value and self.bank_.check_reliability():
            self.amount_ -= value
            other_account.amount += value

    def put(self, value):
        self.amount_ += value

    def withdraw(self, value):
        if self.amount_ >= value and self.bank_.check_reliability():
            self.amount_ -= value


class CreditAccount(IAccount):
    def __init__(self, amount, client, bank, commission, limit, not_upper):
        super().__init__(amount, client, bank)
        self.commission_ = commission
        self.limit_ = limit
        self.not_upper_ = not_upper

    def put(self, value):
        self.amount_ += value

    def withdraw(self, value):
        if self.bank_.check_reliability():
            if self.amount_ + self.limit_ >= value or (self.amount_ <= 0 and self.limit_ - self.commission_ >= value):
                self.amount_ -= value
        else:
            if value <= self.not_upper_:
                if self.amount_ + self.limit_ >= value or (self.amount_ <= 0 and self.limit_ - self.commission_ >= value):
                    self.amount_ -= value

    def transfer(self, other_account, value):
        if self.bank_.check_reliability():
            if self.amount_ + self.limit_ >= value or (self.amount_ <= 0 and self.limit_ - self.commission_ >= value):
                self.amount_ -= value
                other_account.amount_ += value
        else:
            if value <= self.not_upper_:
                if self.amount_ + self.limit_ >= value or (self.amount_ <= 0 and self.limit_ - self.commission_ >= value):
                    self.amount_ -= value
                    other_account.amount_ += value


class DepositAccount(IAccount):
    def __init__(self, amount, client, bank, year, month, day):
        super().__init__(amount, client, bank)
        self.date_close_ = [year, month, day]
        self.current_date_ = [int(datetime.now().year), int(datetime.now().month), int(datetime.now().day)]

    def put(self, value):
        self.amount_ += value

    def is_expired(self):
        return self.current_date_[0] >= self.date_close_[0] and self.current_date_[1] >= self.date_close_[1] and self.current_date_[2] >= self.date_close_[2]

    def transfer(self, other_account, value):
        if self.is_expired():
            if self.amount_ >= value and self.bank_.check_reliability():
                self.amount_ -= value
                other_account.amount += value

    def withdraw(self, value):
        if self.is_expired():
            if self.amount_ >= value and self.bank_.check_reliability():
                self.amount_ -= value



class IOpenAccount:
    def create(self, amount, client, bank, year, month, day, commission, limit, not_upper) -> IAccount:
        raise NotImplementedError


class OpenDebit(IOpenAccount):
    def create(self, amount, client, bank, year, month, day, commission, limit, not_upper):
        return DebitAccount(amount, client, bank)


class OpenCredit(IOpenAccount):
    def create(self, amount, client, bank, year, month, day, commission, limit, not_upper):
        return CreditAccount(self, amount, client, bank, commission, limit, not_upper) #поправить


class OpenDeposit(IOpenAccount):
    def create(self, amount, client, bank, year, month, day, commission, limit, not_upper):
        return DepositAccount(self, amount, client, bank, year, month, day) #поправить
