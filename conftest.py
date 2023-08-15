import pytest
import json


@pytest.fixture
def new_json_file():
    with open('tests/test.json', 'w') as file:
        json.dump([{'test': 'test'}], file)


@pytest.fixture
def dict_list():
    array = [
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {
                "amount": "56516.63",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        },
        {
            "id": 743278119,
            "state": "EXECUTED",
            "date": "2018-10-15T08:05:34.061711",
            "operationAmount": {
                "amount": "51203.12",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1435442169918409",
            "to": "Maestro 7452400219469235"
        },
    ]
    return array


@pytest.fixture
def filtered_dict_list():
    array = [
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {
                "amount": "56516.63",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 743278119,
            "state": "EXECUTED",
            "date": "2018-10-15T08:05:34.061711",
            "operationAmount": {
                "amount": "51203.12",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1435442169918409",
            "to": "Maestro 7452400219469235"
        },
    ]
    return array


@pytest.fixture
def sorted_dict_list():
    array = [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {
                "amount": "56516.63",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847"
        },
        {
            "id": 743278119,
            "state": "EXECUTED",
            "date": "2018-10-15T08:05:34.061711",
            "operationAmount": {
                "amount": "51203.12",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1435442169918409",
            "to": "Maestro 7452400219469235"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        },
    ]
    return array
