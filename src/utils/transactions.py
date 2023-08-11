class Transactions:
    def __init__(self, all_trans: list):
        self.all_trans = all_trans

    def take_statistic(self):
        transactions = []
        for transaction in self.all_trans:
            string = self.__get_transaction_form(transaction)
            transactions.append(string)
        return transactions

    def __build_account(self, string: str) -> str:
        split_str = string.split()
        if len(split_str[-1]) == 20:
            account_number = '**' + split_str[-1][-4:]
            name_number = string[:-20]
            return name_number + account_number
        else:
            account_number = split_str[-1][:4] + ' ' + split_str[-1][4:6] + '** **** ' + split_str[-1][-4:]
            name_number = string[:-16]
            return name_number + account_number

    def __get_from(self, dictionary: dict):
        return self.__build_account(dictionary.get('from'))

    def __get_to(self, dictionary: dict):
        return self.__build_account(dictionary.get('to'))

    def __get_date(self, dictionary: dict) -> str:
        date_time = dictionary.get('date').split('T')
        day = date_time[0].split('-')[2]
        month = date_time[0].split('-')[1]
        year = date_time[0].split('-')[0]
        return day + '.' + month + '.' + year

    def __get_transaction_form(self, dictionary: dict) -> str:
        if dictionary.get('from') is None:
            return (f"{self.__get_date(dictionary)} {dictionary.get('description')}\n"
                    f"{self.__get_to(dictionary)}\n"
                    f"{dictionary['operationAmount']['amount']} "
                    f"{dictionary['operationAmount']['currency']['name']}\n")
        else:
            return (f"{self.__get_date(dictionary)} {dictionary.get('description')}\n"
                    f"{self.__get_from(dictionary)} -> {self.__get_to(dictionary)}\n"
                    f"{dictionary['operationAmount']['amount']} "
                    f"{dictionary['operationAmount']['currency']['name']}\n")
