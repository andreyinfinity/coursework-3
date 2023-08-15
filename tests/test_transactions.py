from src.utils.transactions import Transactions


def test_take_statistic(sorted_dict_list):
    assert Transactions(sorted_dict_list).take_statistic() == ['08.12.2019 Открытие вклада\nСчет **5907\n'
'41096.24 USD\n',
'22.12.2018 Перевод с карты на карту\n'
'Visa Gold 8326 53** **** 6459 -> MasterCard 6783 91** **** 1847\n'
'56516.63 USD\n',
'15.10.2018 Перевод с карты на карту\n'
'MasterCard 1435 44** **** 8409 -> Maestro 7452 40** **** 9235\n'
'51203.12 USD\n',
'12.09.2018 Перевод организации\n'
'Visa Platinum 1246 37** **** 3588 -> Счет **1657\n'
'67314.70 руб.\n']
