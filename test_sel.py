import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("no-sandbox")
options.add_argument("headless")
options.add_argument("window-size=1800,1000")
se =  Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
driver = webdriver.Chrome(options=options, service=se)

driver.get("http://localhost")

def wait_for_element_by_class_name(class_name, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
        return element
    except TimeoutException:
        return None

""""
-First test-
The function checks that the words I entered appear at the top and bottom of the image
"""""
def test_1():
    # Fills in the first text
    text1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/input[1]')
    text1.click()
    text1.send_keys("GOOD")

    # fills in the second text
    text2 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/input[2]')
    text2.click()
    text2.send_keys("TEAM")
    
    # Pressing a button that generates
    button = driver.find_element(By.CLASS_NAME, "gen-btn").click()
    
     # Waiting for the "mem-img" element to load
    image_element = wait_for_element_by_class_name("mem-img")
    assert image_element is not None, "Image element not found!"

    # Waiting for the image to load, and checking the first text
    result1 = driver.find_element(By.CLASS_NAME,"top").text
    assert result1 == "GOOD", "Wrong result, Does not display the required word!"

    # Waiting for the image to load, and checking the second text
    result2 = driver.find_element(By.CLASS_NAME,"bottom").text
    assert result2 == "TEAM", "Wrong result, Does not display the required word!"

"""""
-Second test-
The function checks that the images change after pressing the button that generates
"""""
def test_2():
    
    # Waiting for the "mem-img" element to load
    image_element = wait_for_element_by_class_name("mem-img")
    assert image_element is not None, "Image element not found!"

    # Checking the source of the image before clicking the button
    result3 = driver.find_element(By.CLASS_NAME,"mem-img").get_attribute("src")
    print(result3)

    # Pressing a button that generates
    button = driver.find_element(By.CLASS_NAME, "gen-btn").click()

    # Waiting for the "mem-img" element to load
    image_element = wait_for_element_by_class_name("mem-img")
    assert image_element is not None, "Image element not found!"
    
    # Checking the source of the image after clicking the button
    result4 = driver.find_element(By.CLASS_NAME,"mem-img").get_attribute("src")
    print(result4)

    # Checking that the sources of the image are different
    assert result3 != result4, "Wrong result, Showing the same image!"

"""""
-Third test-
Close the driver at the end of all tests
"""""
def test_exit():
    driver.quit()

