from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_url(search):
    url = 'https://search.naver.com/search.naver?where=realtime&sm=tab_rea&query=검색어&ie=utf8&best=0'.replace('검색어', search)
    return url

def search(url):


    chromedriver = 'C:\\ProgramData\\Anaconda3\\chromedriver.exe' # 윈도우 
    driver = webdriver.Chrome(chromedriver)

    driver.get(url)

    load_button = driver.find_element_by_class_name('_moreBtn')
    for i in range(10):
        load_button.click()
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(0.2)

    text = driver.find_elements_by_class_name('txt_link')

    word_list = []

    for i in range(30):
        # print(text[i].text)
        word_list.append(text[i].text)
    # time.sleep(5)
    return word_list

# driver.quit()

# print(get_url('포항 지진'))

# print(search(get_url('지진')))