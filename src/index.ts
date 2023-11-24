import metadata from '../countries_metadata.json';

export interface Country {
    code: string;
    flag: string;
    name: string;
    dial_code: string;
    currency_code: string;
    continent: string;
    capital: string;
}

export const countries: Country[] =  metadata

export function findCountryByCode(code: string): Country | undefined {
    return countries.find(country => country.code === code);
}

export function getCountryByName(name: string): Country | undefined {
    return countries.find(country => country.name === name);
}

export function findCountriesByContinent(continent: string): Country[] {
    return countries.filter(country => country.continent === continent);
}