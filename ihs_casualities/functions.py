import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from ihs_casualities.server import LOGIN_URL, USERNAME, PASSWORD


def login_to_website():
    try:
        options = Options()
        options.headless = True
        service = Service("chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(LOGIN_URL)
        time.sleep(2)

        driver.find_element("id", "Username").send_keys(USERNAME)
        driver.find_element("id", "Password").send_keys(PASSWORD)
        driver.find_element("id", "btnLogInIdx").click()
        print('login successfully')
        # Navigate to the desired link
        driver.get(
            "https://maritime.ihs.com/Areas/Seaweb/authenticated/authenticated_handler.aspx?control=eventssearch&bp=1"
            "&type=clear")
        print('enter to link successfully')

        # Wait for the element to become clickable
        start_date_from_field = driver.find_element("id", "ctl00_StartDateFrom")
        actions = ActionChains(driver)
        actions.move_to_element(start_date_from_field).click().perform()
        print('select date field successfully')

        # Wait for the year dropdown to be present
        wait = WebDriverWait(driver, 10)
        year_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@class='ui-datepicker-year']")))

        year_select = Select(year_dropdown)
        year_select.select_by_value("2023")

        print('Find the year dropdown and select the desired year successfully')

    except Exception as e:
        print('Failed with Exception: ' + str(e))
