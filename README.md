# Currency Converter (CLI Application)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7ff729f29a26451bb845929a87966750)](https://app.codacy.com/gh/mongare70/Currency-Converter-CLI-Application-PyInquirer?utm_source=github.com&utm_medium=referral&utm_content=mongare70/Currency-Converter-CLI-Application-PyInquirer&utm_campaign=Badge_Grade_Settings)

>A project done in fulfillment of the first checkpoint of the SkaeHub Developer Program

#1 Problem definition
The main objective of this project is to model a Currency Converter application that converts currencies using the latest rates.

## How?
It converts the amount the user has entered from the added base currency to the added result currency.
It then prints out a JSON containing the converted currency.

## Which API?
This application uses Rapid API's Currency Converter API 
to convert the currency using the latest currency rates.
  
### The supported currencies for this application are:
  * Kenyan Shilling (KES)
  * U.S. Dollar (USD)
  * European Euro (EUR)
  * Japanese Yen (JPY)
  * British Pound (GBP)
  * Swiss Franc (CHF)
  * Canadian Dollar (CAD)
  * Australian Dollar (AUD)
  * New Zealand Dollar (NZD)
  * South African Rand (ZAR)

#2. Installation and setup

1. First clone this repository to your local machine using `https://github.com/mongare70/Currency-Converter-CLI-Application`

2. Checkout into the **master** branch using `git checkout master`

3. Create a **virtualenv** on your machine and install the dependencies via `pip install -r requirements.txt` and activate it.

4. cd into the **app** folder and run `python currency_converter_cli.py`


#3. Commands

The following are the commands used in this program:

1. *cconverter run*
2. *cconverter quit*


#4. Usage
The following screencast shows how to run the app. Check it out:

https://user-images.githubusercontent.com/46082842/124652461-d7b68d00-dea4-11eb-8b6f-ee4cd140025b.mp4



#5. Tests

To run tests ensure that you are within the *virtual environment* and have the following installed:

1. *pytest*
2. *pytest-cov*

After ensuring the above, within the **app folder** run :

`pytest` or

`pytest --cov=test_currency_converter_cli`
  

## Credits

1. [Hillary Mongare](https://github.com/mongare70)

2. The [SkaeHub](https://skaehub.com/) community.

