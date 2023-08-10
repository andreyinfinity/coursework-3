class Transaction:
    def __init__(self, dictionary):
        self.date = dictionary.get('date')
        self.description = dictionary.get('description')
        self.__from_whom = dictionary.get('from')
        self.__to_whom = dictionary.get('to')
        self.amount = dictionary['operationAmount']["amount"]
        self.currency = dictionary['operationAmount']['currency']['name']

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
        if self.__from_whom is None:
            return (f"{self.get_date()} {self.description}\n"
                    f"{self.get_to()}\n"
                    f"{self.amount} {self.currency}\n")
        else:
            return (f"{self.get_date()} {self.description}\n"
                    f"{self.get_from()} -> {self.get_to()}\n"
                    f"{self.amount} {self.currency}\n")
