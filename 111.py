# пример использования декоратора
import requests
import xmltodict
import time
from datetime import datetime

def timeall(func):
  start = time.time()
  func()
  end = time.time()
  print('[*] Время выполнения: {} секунд.'.format(end - start))

@timeall
def cbr_usd_api():
  day = datetime.now().strftime("%d")
  mounth = datetime.now().strftime("%m")
  year = datetime.now().strftime("%Y")
  url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{mounth}/{year}'
  xml = xmltodict.parse(requests.get(url).content)

  for value in xml['ValCurs']['Valute']:
    if value['@ID'] == 'R01235':
      print ('Курс доллара: {} руб.'.format(value['Value'][:5]))



