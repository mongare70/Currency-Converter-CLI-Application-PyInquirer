import requests

def get_available_currencies():
    url = "https://currency-converter5.p.rapidapi.com/currency/list"

    headers = {
        'x-rapidapi-key': "4d9f466073mshb8ba8203587047cp1577edjsnca88f2829b4e",
        'x-rapidapi-host': "currency-converter5.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response.text

response_json = get_available_currencies()


# print result
print(response_json)