import requests
import  pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def browser():
   chrome_browser = webdriver.Chrome()
   return chrome_browser()                       #Выполняется при вызове её в параметре тестовой функции автоматически

def check_Botton(browser()):
    #browser = webdriver.Chrome()
    browser.get('https://www.qa-practice.com/elements/button/simple')
    browser.find_element(By.ID, 'submit-id-submit').click()
    assert browser.find_element(By.ID, 'result-text').is_displayed()
    


check_Botton(browser())