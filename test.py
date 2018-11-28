import requests
from datetime import datetime, date, timedelta
import calendar
import time
import random


url = 'http://market.finance.sina.com.cn/transHis.php?symbol=sz000333&date=2017-07-17&page=1'
code = 'sz000333'
first_day = '2017-01-01'
last_day = '2017-02-02'


def get_headers():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    user_agent = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )

    headers = {
        'User-Agent':user_agent

    }
    print(headers)
    return headers

def date_generator(first_day, last_day, format='%Y-%m-%d'):
    first_day = datetime.strptime(first_day, format)
    last_day = datetime.strptime(last_day, format)
    days = (last_day - first_day).days
    for i in range(0, days):
        day = first_day +timedelta(i)
        day = datetime.strftime(day, format)
        yield day



def url_generator(code, page):
    '''date: 2017-01-01'''
    for date in date_generator(first_day, last_day):
        url = 'http://market.finance.sina.com.cn/transHis.php?symbol={}&date={}&page={}'.format(code, date, page)
        yield url

def get_pages():
    for url in url_generator(code,1):
        headers = get_headers()
        time.sleep(1)
        response = requests.get(url,headers=headers)
        print(response.content)



# get_pages()

# date_generator(first_day,last_day)

# get_pages()



test = requests.get('http://quotes.money.163.com/service/chddata.html?code=1000333&start=20170101&end=20180101&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER ')

print(test.text)
with open('meidi.csv','w') as f:
    f.write(test.text)

