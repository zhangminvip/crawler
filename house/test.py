# coding:utf-8
import time
from selenium import webdriver
import time


def extract_data():
    # years = driver.find_element_by_id('gb-year').find_elements_by_tag_name('option')
    # for year in years[0:3]:
    #     year.click()
    #     months = driver.find_element_by_id('gb-month').find_elements_by_tag_name('option')
    #     for month in months:
    #         month.click()
    units = driver.find_element_by_id('gb-unit').find_elements_by_tag_name('li')
    units[2].click()

    search_btn = driver.find_element_by_css_selector("[class='gb-btn gb-searchBtn']")
    search_btn.click()
    time.sleep(3)
    # print(driver.current_url)
    tbody = driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    # print(len(trs))
    for tr in trs[1:]:
        # print(tr.text)
        ths = tr.find_elements_by_tag_name('th')
        print(ths[1].text, ths[2].text, ths[3].text, ths[4].text)


driver = webdriver.Chrome(
    '/home/minzhang/PycharmProjects/sina_finance/house/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.creprice.cn/proprice/pchebei.html')
driver.get('http://www.creprice.cn/rank/index.html')
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

driver.implicitly_wait(30)
# driver.maximize_window()
# province = driver.find_element_by_class_name('gb-provinceList').find_elements_by_css_selector("[class='gb-selectItem2 gb-select']")
provinces = driver.find_element_by_class_name('gb-provinceList').find_elements_by_css_selector(
    "[class='gb-selectItem2']")
print('***省总长度***', len(provinces))
for p in provinces:
    print('***省***' + p.text)
    p.click()
    selected_p = p.text
    cities = driver.find_element_by_class_name('gb-cityList').find_elements_by_class_name('gb-selectItem2')
    if cities:
        for city in cities:
            city.click()
            selected_c = city.text
            print('***城市***', selected_c)
            extract_data()
    else:
        selected_c = ''
        print('***城市***', selected_c)
        extract_data()


