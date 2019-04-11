import requests

currency_list = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
print(currency_list)