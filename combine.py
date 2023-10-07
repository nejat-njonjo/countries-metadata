import json
from typing import List


def load_file(filename: str) -> dict:
    with open(f'./assets/{filename}.json', 'r', encoding='utf8') as file:
        return json.load(file)

def save_list(data: List, filename: str) -> bool:
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(data, file)
    return True

def find_in(data: List[dict], match: str, value: str) -> dict:
    for item in data:
        if item[match] == value:
            return item
    return None

def process_countries(countries: List[dict], emojis: List[dict], currencies: List[dict]) -> List[dict]:
    countries_metadata = []
    for country in countries:
        data = find_in(emojis, 'code', country['code'])
        flag = data['emoji'] if data else ''

        # Find currency info for the current country
        currency_info = next((c for c in currencies if c['countryCode'] == country['code']), None)
        currency_code = currency_info['currencyCode'] if currency_info else ''

        country_info = {
            'code': country['code'],
            'flag': flag,
            'name': country['name'],
            'dial_code': country['dial_code'],
            'currency_code': currency_code
        }
        countries_metadata.append(country_info)

    return countries_metadata


def main():
    emojis = load_file('emojis')
    currencies = load_file('currencies')
    countries = load_file('CountryCodes')

    countries_metadata = process_countries(countries, emojis, currencies)
    save_list(countries_metadata, 'countries_metadata.json')

if __name__ == '__main__':
    main()
