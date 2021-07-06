# import libraries
from PyInquirer import style_from_dict, Token, prompt, Separator
from prompt_toolkit.validation import Validator, ValidationError
from termcolor import colored
from pprint import pprint
import sys, os
import json
import requests

# python module for converting strings into ASCII Text with arts fonts
from pyfiglet import Figlet

f = Figlet(font='doom')
print('--------------------------------------------------------------------------------------------------------------')
print(colored(f.renderText('Currency Converter'),'yellow'))

print('\n''-------------Supported Currencies----------------' '\n')
print('   1. Kenyan Shilling (KES) ')
print('   2. U.S. Dollar (USD) ')
print('   3. European Euro (EUR) ')
print('   4. Japanese Yen (JPY) ')
print('   5. British Pound (GBP) ')
print('   6. Swiss Franc (CHF) ')
print('   7. Canadian Dollar (CAD) ')
print('   8. Australian Dollar (AUD) ')
print('   9. New Zealand Dollar (NZD) ')
print('   10. South African Rand (ZAR) ')

print('\n''-------------USAGE----------------' '\n')
print('   1."python app/currency_converter.py" ---> to run the app')
print('   2."cconverter run" --> to start the app')
print('   3."cconverter quit" ---> To close the app' '\n')
print('-------------------------------------------------------------------------------------------------------------')


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


#prompting user for a command
command = input('Enter a command: ' '\n')

def currency_converter():
    
    if command == 'cconverter run':

        def cconverter():

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
                            'name' : 'KES'
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
                            'name' : 'KES'
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


            # currency convert class
            class CurrencyConverter:
                def __init__(self, base_currency, result_currency, amount_to_convert):
                    self.base = base_currency
                    self.result = result_currency
                    self.amount = amount_to_convert


                # Convert currency method
                def convert(self):
                    
                    # check if base, result, and amount have been parsed
                    if self.base and self.result and self.amount:

                        # check if amount is integer or float
                        if isinstance(self.amount, int) or isinstance(self.amount, float):
                            url = "https://currency-converter5.p.rapidapi.com/currency/convert"

                            querystring = {"format":"json","from":self.base,"to":self.result,"amount":"{}".format(self.amount)}

                            headers = {
                                'x-rapidapi-key': "4c7fdf69eemsh8d6039574576e92p17fed4jsnf84661b04230",
                                'x-rapidapi-host': "currency-converter5.p.rapidapi.com"
                            }

                            response = requests.request("GET", url, headers=headers, params=querystring)

                            # return response
                            return response.text
                        
                        else:
                            return False

                    else:
                        return False

            # create object       
            transaction = CurrencyConverter(answers['base currency'], answers['result currency'], answers['amount to convert'])

            # convert currency and put it into a dictionary
            response = json.loads(transaction.convert())

            # print result
            print('Result:',response["rates"])
    
        return cconverter()

    #closing the app when user enters the quit command
    elif command == 'cconverter quit':
        f = Figlet(font='doom')
        print(colored(f.renderText('GoodBye , Thanks for using Currency Converter !'),'yellow'))
        sys.exit()

    #restarting the app if user inputs an invalid command
    else:
        print('Invalid Command!')
        print('Try Again' '\n')
        os.execv(sys.executable, ['python'] + sys.argv)


if __name__ == '__main__':
    currency_converter()
    while True:
        questions = [
            {
                'type':'confirm',
                'name':'continue',
                'message': 'Do Want to Continue Using Currency Converter?',
                'default': False
            }   
        ]
        answer = prompt(questions, style=style)
        answer = answer['continue']
        if answer:
            currency_converter()
        else:
            f = Figlet(font='doom')
            print(colored(f.renderText('GoodBye , Thanks for using Currency Converter !'),'yellow'))
            break