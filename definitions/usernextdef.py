from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.buttons_locators import Button_Locators
from definitions.driverdef import DriverDef

class Confirm_Pay_Tpin(DriverDef):
      
      #   def __init__(self,driver):
      #           self.driver=driver
      #           self.wait=WebDriverWait(driver,30)

        def confirm_button(self):
           spin_btn=self.wait.until(EC.element_to_be_clickable(Button_Locators.confirm_xpath))
           assert (spin_btn.text=="Confirm"),"Click on confirm button"
           spin_btn.click()
        def pay_button(self):
           pay_btn=self.wait.until(EC.presence_of_element_located(Button_Locators.pay_xpath))
           assert (pay_btn.get_attribute("type")=="submit"),"Click on paybutton to submit your payment"
           pay_btn.click()
        def tpin_field(self,tpin):
           tpin_input=self.wait.until(EC.element_to_be_clickable(Button_Locators.tpinfield))
           assert (tpin_input.get_attribute("inputmode")=="numeric"),"Enter tpin only in numeric format"
           tpin_input.send_keys(tpin)
        def done_button(self):
           self.wait.until(EC.presence_of_element_located(Button_Locators.done_xpath)).click()
