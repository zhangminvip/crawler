import requests
import datetime

PROVINCE_NAME=['pcanhui','pcguangxi']
now = datetime.datetime.now()
base_url = 'http://www.creprice.cn'

def gen_all_url():
    for pr in PROVINCE_NAME:
        for year in range(now.year, 2007, -1):
            for month in range(12, 0, -1):
                pr['url'] = "%s/proprice/pc%s-ti%d%02d.html" % (base_url, pr, year, month)
                pr['year'] = year
                pr['month'] = month
                yield pr
for url in gen_all_url():
    print (url)