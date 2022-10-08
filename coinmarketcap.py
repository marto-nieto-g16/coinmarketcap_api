 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5dfa85a4-aa37-4df6-a281-49beed4bbe7a',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  for crypos_list in data['data']:
    if crypos_list['symbol'] == 'BNB':
      
      Low_1hr = crypos_list['quote']['USD']['price'] - crypos_list['quote']['USD']['percent_change_1h']
      High_1hr = crypos_list['quote']['USD']['price'] + crypos_list['quote']['USD']['percent_change_1h']

      Low_24hr = crypos_list['quote']['USD']['price'] - crypos_list['quote']['USD']['percent_change_24h']
      High_24hr = crypos_list['quote']['USD']['price'] + crypos_list['quote']['USD']['percent_change_24h']

      datos_crypto = {'Name':[crypos_list['name']],
      'Symbol':[crypos_list['symbol']],
      'Price': [crypos_list['quote']['USD']['price']],
      'Low_1hr':[Low_1hr],
      'High_1hr':[High_1hr],
      'Low_24hr':[Low_24hr],
      'High_24hr':[High_24hr],
      'Time':['o']
      }

      df = pd.DataFrame(datos_crypto)
      print(df)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  