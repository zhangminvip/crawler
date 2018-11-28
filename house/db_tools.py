#coding:utf-8
from sqlalchemy import create_engine


province = '安徽'
city= '合肥'
year = '2018'
month = '12'
price = 23
url = 'ssss'

DIALCT = "mysql"
DRIVER = "pymysql"
USERNAME = "root"
PASSWORD = "123456"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "house"
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
print(DB_URI)
engine = create_engine(DB_URI)
con = engine.connect()

def insert(province, city,year,month,price,url):

    str = "INSERT INTO residential (province,city,year,month,price,url) VALUES ('{}','{}','{}','{}','{}','{}');".format(province,city,year,month,price,url)
    print(str)
    # result = con.execute("INSERT INTO residential (province,city,year,month,price,url) VALUES ('安 徽','合肥','2018','12',10,'slf')")
    con.execute(str)
    # print(result.fetchone())
