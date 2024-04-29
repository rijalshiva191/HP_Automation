from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.loginpage_locators import Loginpage_locators 
from definitions.driverdef import DriverDef

class Login_HP(DriverDef):
    
    # def __init__(self,driver):
    #     self.driver=driver
    #     self.wait = WebDriverWait(driver, 30)
        
    def open_page(self,url):
        self.driver.get(url)
    
    def email_input(self,email):
        email_input_field = self.wait.until(EC.presence_of_element_located(Loginpage_locators.email_inputfield))
        email_field = email_input_field.get_attribute("type")
        assert (email_field=="email"),"This field is not of email input field type."
        email_input_field.send_keys(email)

    def password_input(self,password):
        pas_input = self.wait.until(EC.presence_of_element_located(Loginpage_locators.password_field))
        assert (pas_input.get_attribute("type")=="password"),"This field is not of password type."
        pas_input.send_keys(password)

    def signin(self):
        signinButton= self.wait.until(EC.presence_of_element_located(Loginpage_locators.signin_button))
        assert (signinButton.text=="Sign In With Google"),"Sign in button didnot found"
        signinButton.click()
        # self.driver.find_element(*self.signin_button).click()
    def next(self):
        next_btn=self.wait.until(EC.presence_of_element_located(Loginpage_locators.next_button))
        assert (next_btn.text =="Next"),"Button name did not matched"
        next_btn.click()
    
    #   self.driver.find_element(*self.next_button).click()
    def password_next(self):
        pas_next=self.wait.until(EC.presence_of_element_located(Loginpage_locators.password_nextbutton))
        assert (pas_next.text=="Next"),"Button name did not matched"
        pas_next.click()
