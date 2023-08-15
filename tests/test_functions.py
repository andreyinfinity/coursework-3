from src.utils.functions import load_file, filter_dictionary_list, sorted_dictionary_list


def test_load_file(new_json_file):
    assert load_file('tests/test.json') == [{'test': 'test'}]


def test_filter_dictionary_list(dict_list, filtered_dict_list):
    assert filter_dictionary_list(dict_list, 'state', 'EXECUTED') == filtered_dict_list


def test_sorted_dictionary_list(dict_list, sorted_dict_list):
    assert sorted_dictionary_list(dict_list, 'date') == sorted_dict_list
