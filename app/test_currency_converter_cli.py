import unittest
from currency_converter_cli import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):
    # test with no arguments 
    def test_convert_no_argument(self):
        self.assertFalse(CurrencyConverter('', '', '').convert())

    # test with only base argument 
    def test_convert_only_base(self):
        self.assertFalse(CurrencyConverter('KES', '', '').convert())

    # test with only result argument
    def test_convert_only_result(self):
        self.assertFalse(CurrencyConverter('', 'USD', '').convert())

    # test with all arguments
    def test_convert_all_arguments(self):
        self.assertAlmostEqual(CurrencyConverter("KES", "USD", 10000).convert(),
        {'USD': {"currency_name": "United States dollar", "rate": "0.0093", "rate_for_amount": "92.7734"}})

    # test with all arguments lowercase
    def test_convert_all_arguments(self):
        self.assertAlmostEqual(CurrencyConverter("kes", "usd", 10000).convert(),
        {'USD': {"currency_name": "United States dollar", "rate": "0.0093", "rate_for_amount": "92.7734"}})

    # test with wrong base argument
    def test_convert_wrong_base(self):
        self.assertFalse(CurrencyConverter("HHH", "USD", 10000).convert())

    # test with wrong result argument
    def test_convert_wrong_result(self):
        self.assertFalse(CurrencyConverter("KES", "HHH", 10000).convert())

    # test with wrong amount argument
    def test_convert_wrong_amount(self):
        self.assertFalse(CurrencyConverter("KES", "USD", 'HHHH').convert())

    # test with wrong base argument & result argument
    def test_convert_wrong_base_and_result(self):
        self.assertFalse(CurrencyConverter("HHH", "HHH", 10000).convert())

    # test with wrong base argument & amount argument
    def test_convert_wrong_base_and_amount(self):
        self.assertFalse(CurrencyConverter("HHH", "USD", 'HHH').convert())

    # test with wrong base argument & result argument
    def test_convert_wrong_result_and_amount(self):
        self.assertFalse(CurrencyConverter("KES", "HHH", 'HHH').convert())

    # test with all wrong arguments
    def test_convert_wrong_all(self):
        self.assertFalse(CurrencyConverter("HHH", "HHH", 'HHH').convert())
    

# if __name__ == '__main__':
#     unittest.main()