import requests

json_dict = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
currency_list = json_dict['Valute']
for item in currency_list:
    print(currency_list[item])