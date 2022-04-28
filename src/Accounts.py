from datetime import datetime


class IAccount:
    def __init__(self, amount, client, bank, not_upper):
        self.amount_ = amount
        self.client_ = client
        self.bank_ = bank
        self.not_upper_ = not_upper

    def transfer(self, other_account, value):
        raise NotImplementedError

    def withdraw(self, value):
        raise NotImplementedError

    def put(self, value):
        raise NotImplementedError

    def show_amount(self):
        raise NotImplementedError


class DebitAccount(IAccount):
    def __init__(self, amount, client, bank, not_upper):
        super().__init__(amount, client, bank, not_upper)

    def transfer(self, other_account, value):
        self.withdraw(value)
        other_account.put(value)

    def put(self, value):
        self.amount_ += value

    def withdraw(self, value):
        if self.amount_ < value:
            raise Exception("You have no money!")
        if not self.bank_.check_reliability() and value > self.not_upper_:
            raise Exception("You are not reliable!")
        self.amount_ -= value

    def show_amount(self):
        return self.amount_


class CreditAccount(IAccount):
    def __init__(self, amount, client, bank, commission, limit, not_upper):
        super().__init__(amount, client, bank, not_upper)
        self.commission_ = commission
        self.limit_ = limit

    def put(self, value):
        self.amount_ += value

    def withdraw(self, value):
        if not self.bank_.check_reliability() and value > self.not_upper_:
            # ошибка не надежный
            pass
        else:
            if self.amount_ > 0 and (self.amount_ + self.limit_ < value):
                # ошибка нет денег
                pass
            if self.amount_ <= 0 and (self.limit_ + self.amount_ < value + value * self.commission_):
                # ошибка нет денег
                pass
        self.amount_ -= value

    def transfer(self, other_account, value):
        self.withdraw(value)
        other_account.put(value)

    def show_amount(self):
        return self.amount_


class DepositAccount(IAccount):
    def __init__(self, amount, client, bank, year, month, day, not_upper, percent):
        super().__init__(amount, client, bank, not_upper)
        self.date_close_ = [year, month, day]
        self.current_date_ = [int(datetime.now().year), int(datetime.now().month), int(datetime.now().day)]
        self.percent_ = percent

    def put(self, value):
        self.amount_ += value

    def is_expired(self):
        return self.current_date_[0] >= self.date_close_[0] and self.current_date_[1] >= self.date_close_[1] and self.current_date_[2] >= self.date_close_[2]

    def transfer(self, other_account, value):
        self.withdraw(value)
        other_account.put(value)

    def withdraw(self, value):
        if not self.is_expired():
            #ошибка депозит не истек
            pass
        if self.amount_ + self.amount_ * self.percent_ < value:
            #ошибка нет денег
            pass
        if not self.bank_.check_reliability() and value > self.not_upper_:
            #ошибка не надежный
            pass
        if (self.amount_ - value) < 0:
            self.amount_ = self.amount_ + self.amount_ * self.percent_ - value
        else:
            self.amount_ -= value

    def show_amount(self):
        if self.is_expired():
            return self.amount_ + self.amount_ * self.percent_
        else:
            return self.amount_


class ForeignAccount(IAccount):
    def __init__(self, amount, client, bank, not_upper, type_arg, sell_price, buy_price):
        super().__init__(amount, client, bank, not_upper)
        self.type_ = type_arg
        self.sell_price_ = sell_price
        self.buy_price_ = buy_price

    def transfer(self, other_account, value):
        value_rub = self.sell(value)
        other_account.put(value_rub)

    def put(self, value):
        self.amount_ += self.buy(value)

    def withdraw(self, value):
        if value > self.amount_:
            #ошибка нехватки денег
            pass
        if not self.bank_.check_reliability() and value > self.not_upper_:
            #ошибка не надежный
            pass
        self.amount_ -= value

    def sell(self, value):
        return value * self.sell_price_

    def buy(self, value):
        return value / self.buy_price_

    def show_amount(self):
        return self.amount_


class IOpenAccount:
    def create(self, amount, client, bank, year, month, day, commission, limit, not_upper, type_arg, sell_price, buy_price, percent) -> IAccount:
        raise NotImplementedError


class OpenDebit(IOpenAccount):
    def create(self, amount, client, bank, year, month, day, commission, limit, not_upper, type_arg, sell_price, buy_price, percent):
        return DebitAccount(amount, client, bank, not_upper)


class OpenCredit(IOpenAccount):
    def create(self, amount, client, bank, year, month, day, commission, limit, not_upper, type_arg, sell_price, buy_price, percent):
        return CreditAccount(amount, client, bank, commission, limit, not_upper)


class OpenDeposit(IOpenAccount):
    def create(self, amount, client, bank, year, month, day, commission, limit, not_upper, type_arg, sell_price, buy_price, percent):
        return DepositAccount(amount, client, bank, year, month, day, not_upper, percent)


class OpenForeign(IOpenAccount):
    def create(self, amount, client, bank, year, month, day, commission, limit, not_upper, type_arg, sell_price, buy_price, percent):
        return ForeignAccount(amount, client, bank, not_upper, type_arg, sell_price, buy_price)

