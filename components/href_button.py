from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def href_button(driver, href_value, timeout=10):
    wait = WebDriverWait(driver, timeout)
    xpath = f"//a[contains(@href, '{href_value}')]"
    print (f"🔗 Mencari elemen dengan href yang mengandung: {href_value}")
    time.sleep(5) 
    try:
        module_link = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        module_link.click()
        print (f"melakukan click")
    except Exception as e:
        raise Exception(
            f"Module with href containing '{href_value}' not found or not clickable: {e}"
        )
