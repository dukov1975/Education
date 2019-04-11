import requests

proxy = {'http': 'http://proxy1.lab.test:3128',
         'https': 'https://proxy1.lab.test:3128'}

json_dict = requests.get('https://www.cbr-xml-daily.ru/daily_json.js', proxies=proxy).json()
currency_list = json_dict['Valute']
for item in currency_list:
    print(currency_list[item])