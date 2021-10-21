import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class Test_bitcoin_rates(TestCase):

    @patch('bitcoin.api_call')
    def test_convert_dollars(self, mock_bitcoin_api):

        mock_bitcoin_api.return_value = {"time": {
        "updated": "Oct 21, 2021 03:18:00 UTC",
        "updatedISO": "2021-10-21T03:18:00+00:00",
        "updateduk": "Oct 21, 2021 at 04:18 BST"
        },
        "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName": "Bitcoin",
        "bpi": {
        "USD": {
        "code": "USD",
        "symbol": "&#36;",
        "rate": "64,474.5200",
        "description": "United States Dollar",
        "rate_float": 64474.52
        },
        "GBP": {},
        "EUR": {}
        }
        }

        expected_dollars = 644745.2
        dollars = bitcoin.get_bitcoin_value(10, 64474.5200)
        self.assertEqual(expected_dollars, dollars)

    @patch('bitcoin.api_call')
    def test_if_correct_rate_is_returned(self, mock_bitcoin_api):

        data = mock_bitcoin_api.return_value = {"time":{"updated":"Oct 21, 2021 03:18:00 UTC",
        "updatedISO":"2021-10-21T03:18:00+00:00","updateduk":"Oct 21, 2021 at 04:18 BST"},
        "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName":"Bitcoin","bpi":{
            "USD":{"code":"USD","symbol":"&#36;","rate":"64,474.5200","description":"United States Dollar","rate_float":64474.52},
            "GBP":{"code":"GBP","symbol":"&pound;","rate":"46,630.8742","description":"British Pound Sterling","rate_float":46630.8742},
            "EUR":{"code":"EUR","symbol":"&euro;","rate":"55,275.4889","description":"Euro","rate_float":55275.4889}}}

        expected_rate = 64474.5200
        usd = bitcoin.extract_dollar_rate(data)
        self.assertEqual(expected_rate, usd)


    @patch('bitcoin.api_call')
    def test_api_call(self, mock_bitcoin_api):

        data = mock_bitcoin_api.return_value = {"time":{"updated":"Oct 21, 2021 03:18:00 UTC",
        "updatedISO":"2021-10-21T03:18:00+00:00","updateduk":"Oct 21, 2021 at 04:18 BST"},
        "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName":"Bitcoin","bpi":{
            "USD":{"code":"USD","symbol":"&#36;","rate":"64,474.5200","description":"United States Dollar","rate_float":64474.52},
            "GBP":{"code":"GBP","symbol":"&pound;","rate":"46,630.8742","description":"British Pound Sterling","rate_float":46630.8742},
            "EUR":{"code":"EUR","symbol":"&euro;","rate":"55,275.4889","description":"Euro","rate_float":55275.4889}}}

        returned_data = bitcoin.api_call()
        self.assertEqual(data, returned_data)

    @patch('bitcoin.print')
    def test_display(self, mock_print):
        bitcoins = 50
        value = 3223726

        expected_print = '50.0 Bitcoin is worth $3223726'

        returned=bitcoin.display_exchange_rate(bitcoins, value)
        mock_print.asser_has_calls(expected_print)

    @patch('builtins.input', side_effect=['-1', '-100','-0.5', '0.5'])
    def test_non_positive_input(self, mock_input):
        bitcoins = bitcoin.get_bitcoin()
        self.assertEqual(0.5, bitcoins)


    @patch('builtins.input', side_effect=['hello', '123bitcoin','@$%^', '1'])
    def test_string_and_symbols(self, mock_input):
        bitcoins = bitcoin.get_bitcoin()
        self.assertEqual(1, bitcoins)


if __name__ == '__main__':
    unittest.main()