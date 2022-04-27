class Bank:
    def __init__(self):
        self.name_ = ''
        self.users_ = []
        self.current_client_ = 0
        self.current_account_ = ''
        self.accounts_ = []
        self.client_info = {}

    def check_reliability(self):
        for values in self.client_info[self.current_client_]:
            if len(values) <= 1:
                return False
        return True
