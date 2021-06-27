# import libraries
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from prompt_toolkit.validation import Validator, ValidationError
from pprint import pprint
import json

import requests

# style CLI interface
style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

# validate number input 
class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(message="Please enter a number", cursor_position=len(document.text))

# CLI questions
questions = [
    {
        'type': 'list',
        'message': 'Select base currency',
        'name': 'base currency',
        'choices' : [
            Separator('= The Base Currencies ='),
            {
                'name' : 'KSH'
            },
            {
                'name' : 'USD'
            },
            {
                'name' : 'EUR'
            },
            {
                'name' : 'JPY'
            },
            {
                'name' : 'GBP'
            },
            {
                'name' : 'CHF'
            },
            {
                'name' : 'CAD'
            },
            {
                'name' : 'AUD'
            },
            {
                'name' : 'ZAR'
            },
            {
                'name' : 'NZD'
            },
            {
                'name' : 'BTC'
            }
        ],
        'validate': lambda answer: 'You must choose at least one Base Currency.' \
            if len(answer) == 0 else True
    },
    {
        'type': 'list',
        'message': 'Convert currency to: ',
        'name': 'result currency',
        'choices' : [
            Separator('= The Result Currencies ='),
            {
                'name' : 'KSH'
            },
            {
                'name' : 'USD'
            },
            {
                'name' : 'EUR'
            },
            {
                'name' : 'JPY'
            },
            {
                'name' : 'GBP'
            },
            {
                'name' : 'CHF'
            },
            {
                'name' : 'CAD'
            },
            {
                'name' : 'AUD'
            },
            {
                'name' : 'ZAR'
            },
            {
                'name' : 'NZD'
            },
            {
                'name' : 'BTC'
            }
        ],
        'validate': lambda answer: 'You must choose at least one Result Currency.' \
            if len(answer) == 0 else True
    },
    {
        'type': "input",
        "message": "Enter the amount to convert",
        "name": "amount to convert",
        "validate": NumberValidator,
        "filter": lambda val: int(val)
    }
]

answers = prompt(questions, style=style)
pprint(answers)  # use the answers as input for your app

base_currency = answers['base currency']
result_currency = answers['result currency']
amount_to_convert = answers['amount to convert']

# currency convert class
class CurrencyConverter:
    def currency_convert(self):
        base_currency = answers['base currency']
        result_currency = answers['result currency']
        amount_to_convert = answers['amount to convert']

        url = "https://currency-converter5.p.rapidapi.com/currency/convert"

        querystring = {"format":"json","from":base_currency,"to":result_currency,"amount":"{}".format(amount_to_convert)}

        headers = {
            'x-rapidapi-key': "4d9f466073mshb8ba8203587047cp1577edjsnca88f2829b4e",
            'x-rapidapi-host': "currency-converter5.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response.text
        
# create currency converter object       
currency_converter = CurrencyConverter()

# load json response into a dictionary
response_json = json.loads(currency_converter.currency_convert())

# print result
print(response_json)

