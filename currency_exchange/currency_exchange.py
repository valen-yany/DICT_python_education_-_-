import requests


class CurrencyExchange:

    def __init__(self):
        self.exchange_currency = input().strip()
        self.url = f'http://www.floatrates.com/daily/{self.exchange_currency}.json'
        self.cache = {}
        self.first_request()
        self.exchanging_currency = ''
        while True:
            self.exchange()

    def first_request(self):
        state = False
        response = ''
        while not state:
            response = requests.get(self.url)
            state = response.ok
        response = response.json()
        self.cache.update({'usd': response['usd']['rate']}) if self.exchange_currency != 'USD' else None
        self.cache.update({'eur': response['eur']['rate']}) if self.exchange_currency != 'EUR' else None

    def exchange(self):
        print(self.cache)
        exchanging_currency = input().lower().strip(' ')
        value = int(input())
        if value < 0:
            value = float(input('Enter a right amount of currency\n'))
        print('Checking the cache...')
        if exchanging_currency not in self.cache:
            print('Sorry, but it is not in the cache!')
            bad_state = self.request(exchanging_currency)
            if bad_state:
                print('This currency doesn`t exist!')
                return None
        else:
            print('It is in the cache!')
        print('You received %0.2f %s.' % (self.calc_value(exchanging_currency, value), exchanging_currency.upper()))

        print()

    def request(self, currency):
        response = requests.get(self.url)
        response = response.json()
        if currency not in response.keys():
            return True
        self.cache.update({currency: response[currency]['rate']})

    def calc_value(self, currency, value):

        return self.cache[currency] * value


a = CurrencyExchange()
