from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DriverDef:
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 30)