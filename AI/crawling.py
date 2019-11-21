from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_url(search):
    url = 'https://search.naver.com/search.naver?where=realtime&sm=tab_rea&query=검색어&ie=utf8&best=0'.replace('검색어', search)
    return url


chromedriver = 'C:\\ProgramData\\Anaconda3\\chromedriver.exe' # 윈도우 
driver = webdriver.Chrome(chromedriver)

driver.get(get_url(input('검색어 입력: ')))

text = driver.find_elements_by_class_name('txt_link')

for i in range(5):
    print(text[i].text,end='\n\n')

# driver.quit()

# print(get_url('포항 지진'))