class Transaction:
    def __init__(self, dictionary):
        self.date = dictionary['date']
        self.description = dictionary['description']
        self.__from_whom = dictionary['from_whom']
        self.__to_whom = dictionary['to_whom']
        self.amount = dictionary['amount']
        self.currency = dictionary['currency']['name']

    @classmethod
    def __build_account(cls, string: str) -> str:
        split_str = string.split()
        if len(split_str[-1]) == 20:
            account_number = '**' + split_str[-1][-4:]
            name_number = string[:-20]
            return name_number + account_number
        else:
            account_number = split_str[-1][:4] + ' ' + split_str[-1][4:6] + '** **** ' + split_str[-1][-4:]
            name_number = string[:-16]
            return name_number + account_number

    def get_from(self):
        return self.__build_account(self.__from_whom)

    def get_to(self):
        return self.__build_account(self.__to_whom)

    def get_date(self) -> str:
        date_time = self.date.split('T')
        day = date_time[0].split('-')[2]
        month = date_time[0].split('-')[1]
        year = date_time[0].split('-')[0]
        return day + '.' + month + '.' + year

    def get_transaction_form(self):
        return f"""{self.get_date()} {self.description}\n
            {self.get_from()} -> {self.get_to()}\n
            {self.amount} {self.currency}"""