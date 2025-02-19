from money_converter_config import api_key
from typing import Final
import requests
import json


BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'

def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('rates.json', 'r') as file:
            return json.load(file)

    payload: dict = {'access_key': api_key}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    return data

def get_currency(currency: str, rates: dict) -> float:
    currency: str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        print(f'Currency {currency} not found. Enter a valid currency code(USD/UZS).')

def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)
    print(f'{amount:,.2f} {base.upper()} ->{conversion:,.2f} {vs.upper()}')

def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get('rates')
    try:
        amount_input: float = abs(float(input('Enter amount to convert: ')))
    except ValueError:
        print(f'Amount is not valid. Enter a valid amount(100 or 10).')
        main()

    base_input: str = input('Enter base currency code (USD): ')
    vs_input: str = input('Enter vs currency code (KRW): ')

    convert_currency(amount=amount_input, base=base_input, vs=vs_input, rates=rates)

    # convert_currency(100, base='USD', vs='UZS', rates=rates)
    # convert_currency(100_000, base='KRW', vs='UZS', rates=rates)
    # convert_currency(1_500, base='USD', vs='KRW', rates=rates)

if __name__ == '__main__':
    main()


