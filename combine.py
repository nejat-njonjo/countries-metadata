import json
from typing import List

def save_list(data = [], filename=''):
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(data, file)
    return True


def find_in(list = [], match = '', value = ''):
    found = None
    for item in list:
        if item[match] == value:
            found = item
    return found


def load_emoji_countries() -> List:
    with open('./emojis.json', 'r', encoding='utf8') as emojis_file:
        return json.load(emojis_file)


emojis = load_emoji_countries()

countries_dial_codes = []


with open('CountryCodes.json', 'r', encoding='utf8') as countries_file:
        countries = json.load(countries_file)
        for country in countries:
            data = find_in(emojis, 'code', country['code'])

            if not data:
                countries_dial_codes.append({
                    'code': country['code'],
                    'flag': '',
                    'name': country['name'],
                    'dial_code': country['dial_code']
                })
            else:
                countries_dial_codes.append({
                    'code': country['code'],
                    'flag': data['emoji'],
                    'name': country['name'],
                    'dial_code': country['dial_code']
                })
        save_list(countries_dial_codes, 'countries_dial_code.json')