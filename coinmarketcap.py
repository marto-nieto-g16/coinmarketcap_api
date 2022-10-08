  #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import time

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'Your API',
}

session = Session()
session.headers.update(headers)

def Cryptos(crypto_search):
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    for crypos_list in data['data']:
      if crypos_list['symbol'] == crypto_search :
        
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)

        High_1hr = crypos_list['quote']['USD']['price'] - crypos_list['quote']['USD']['percent_change_1h']
        Low_1hr = crypos_list['quote']['USD']['price'] + crypos_list['quote']['USD']['percent_change_1h']

        High_24hr = crypos_list['quote']['USD']['price'] - crypos_list['quote']['USD']['percent_change_24h']
        Low_24hr = crypos_list['quote']['USD']['price'] + crypos_list['quote']['USD']['percent_change_24h']

        datos_crypto = {'Name':[crypos_list['name']],
        'Symbol':[crypos_list['symbol']],
        'Price': [crypos_list['quote']['USD']['price']],
        'Low_1hr':[Low_1hr ],
        'High_1hr':[High_1hr],
        'Low_24hr':[Low_24hr],
        'High_24hr':[High_24hr],
        'Time':[result]
        }

        df = pd.DataFrame(datos_crypto)
        df.to_csv(crypos_list['name']+'.csv', mode='a')
        
        time.sleep(10)
        return df

  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print("Limit of Credits Earned")

if __name__ == '__main__':
  try:
    while True:
      print(Cryptos('BNB'))
  except KeyboardInterrupt as e:
    print("\n Script Stopped")
