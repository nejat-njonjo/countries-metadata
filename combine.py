import json
from typing import List


def load_json(filename: str) -> dict:
    with open(f'./assets/{filename}.json', 'r', encoding='utf8') as file:
        return json.load(file)


def save_to_json(data: List, filename: str) -> bool:
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(data, file)
    return True


def find_item(data: List[dict], key: str, value: str) -> dict:
    for item in data:
        if item.get(key) == value:
            return item
    return None


def process_countries(countries: List[dict], emojis: List[dict], currencies: List[dict]) -> List[dict]:
    countries_metadata = []
    for country in countries:
        try:
            data = find_item(emojis, 'code', country.get('code'))
            flag = data['emoji'] if data else ''

            # Find currency info for the current country
            currency_info = next((c for c in currencies if c['countryCode'] == country.get('code')), None)
            currency_code = currency_info['currencyCode'] if currency_info else ''

            country_info = {
                'code': country['code'],
                'flag': flag,
                'name': country['name'],
                'dial_code': country['dial_code'],
                'currency_code': currency_code
            }
            countries_metadata.append(country_info)
        except KeyError as e:
            print(f"KeyError: {e} for country: {country}")

    return countries_metadata

def main():
    # Load data from JSON files
    emojis = load_json('emojis')
    currencies = load_json('currencies')
    countries = load_json('CountryCodes')

    # Process countries and save metadata
    countries_metadata = process_countries(countries, emojis, currencies)
    save_to_json(countries_metadata, 'countries_metadata.json')

if __name__ == '__main__':
    main()
