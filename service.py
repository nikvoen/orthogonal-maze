import numpy as np
import requests


# Отправка всей таблицы
def check_equivalence(table):
    def export_to_json(table):
        # Определяем части таблицы
        main_prefixes = ["ε"] + table.S[:table.extended_table].tolist()
        non_main_prefixes = table.S[table.extended_table:].tolist()
        suffixes = ["ε"] + table.E.tolist()

        # Объединяем значения таблицы T построчно
        table_values = [str(value) for row in table._T.values() for value in row]
        table_str = " ".join(table_values)

        # Структура для JSON
        data = {
            "main_prefixes": " ".join(main_prefixes),
            "non_main_prefixes": " ".join(non_main_prefixes),
            "suffixes": " ".join(suffixes),
            "table": table_str
        }

        return data

    url = "http://127.0.0.1:8095/checkTable"
    table_json = export_to_json(table)
    response = requests.post(url, json=table_json)

    if response.status_code == 200:
        get = response.json()['response']
        if get is not None:
            print('!!!!COUNTEREXAMPLE!!!!!')
            return get
        else:
            print('!!!!!WIN!!!!!')
            return "null"
    else:
        print("Ошибка при отправке таблицы", response.status_code)


# Отправка слова
def check_membership(string):
    url = "http://127.0.0.1:8095/checkWord"
    data = {
        "word": string
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        json_response = response.json()['response']
        return json_response
    else:
        print('Ошибка при отправке строки:', response.status_code)

    return ""