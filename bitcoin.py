import requests
 

def main():
    data = api_call()
    bitcoin = get_bitcoin()
    dollar_rate = extract_dollar_rate(data)
    value = get_bitcoin_value(bitcoin, dollar_rate)
    display_exchange_rate(bitcoin, value)


def api_call():
    url='https://api.coindesk.com/v1/bpi/currentprice.json'

    response = requests.get(url)
    data = response.json()

    return data


def get_bitcoin():
    while True:
        try:
            bitcoin = float(input('Enter the number of bitcoin: '))
            if bitcoin >= 0:
                return bitcoin
            else:
                print(' Please enter a number greater than 0')
        except ValueError:
            print('Enter a positive number.')


def extract_dollar_rate(data):
    return data['bpi']['USD']['rate_float']


def get_bitcoin_value(bitcoin, dollar_rate):
    return bitcoin * dollar_rate


def display_exchange_rate(bitcoin, value):
    print(f'{bitcoin} Bitcoin is worth ${value}')


if __name__=='__main__':
    main()