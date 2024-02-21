class Transaction:
    def __init__(self, id_, date, state, operation_amount,  currency_name, currency_code, description, from_, to):
        self.id_ = id_
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.currency_name = currency_name
        self.currency_code = currency_code
        self.description = description
        self.from_ = from_
        self.to = to
        self.is_broken = False
        self.check()

    def check(self):
        check_list = [self.id_, self.date, self.state, self.operation_amount, self.currency_name,
                      self.currency_code, self.description, self.from_, self.to]
        if None in check_list:
            self.is_broken = True
