from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time


def get_html(street_name, url='https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/wait-times.html'):
    try:
        driver = webdriver.Chrome('chromedriver')
        driver.get(url)
        name_box = driver.find_element(By.NAME, value='visawaittimeshomepag_visa_embassysearch_VisaWaitTimesHomePage_input')
        name_box.send_keys(street_name)
        login_button = driver.find_element(By.CLASS_NAME, value="ui-corner-all")
        login_button.click()
        time.sleep(2)
        result = driver.find_element(By.TAG_NAME, value="tbody")
        return result.text
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


if __name__ == "__main__":
    print(get_html('https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/wait-times.html', input('Введите город: ')))
    # if html:
    #     with open("date.html", "w", encoding="utf-8") as f:
    #         f.write(html)

