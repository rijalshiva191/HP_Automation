from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.inputdetails_locators import Inputdetails_Locators 
from definitions.driverdef import DriverDef

class InputDetails(DriverDef):
    # def __init__(self,driver):
    #     self.driver=driver
    #     self.wait=WebDriverWait(driver,30)
    def transfer_optn(self):
        trnsfr_click=self.wait.until(EC.presence_of_element_located(Inputdetails_Locators.money_trnsfr))
        assert (trnsfr_click.text=="Send Money"),"You didnot clicked send money option"
        trnsfr_click.click()
    def send_optn(self):
        send_money_optn=self.wait.until(EC.presence_of_element_located(Inputdetails_Locators.send_optn_path))
        assert (send_money_optn.text=="Hamro Pay Account"),"You didnot clicked hamro pay account option."
        send_money_optn.click()
    def receiver_phno(self,phoneno):
        send_phone=self.wait.until(EC.presence_of_element_located(Inputdetails_Locators.receiver_phone_number))
        assert (send_phone.get_attribute("inputmode")=="numeric"),"Enter phone number only numeric type."
        send_phone.send_keys(phoneno)
    def enter_amount(self,amount):
        send_amount=self.wait.until(EC.presence_of_element_located(Inputdetails_Locators.amount_xpath))
        assert (send_amount.get_attribute("inputmode")=="numeric"),"Enter phone number only numeric type."
        send_amount.send_keys(amount)
    def purpose_click(self):
        self.wait.until(EC.presence_of_element_located(Inputdetails_Locators.purpose_xpath)).click()
    def purpose_dropdown(self):
        self.wait.until(EC.presence_of_element_located(Inputdetails_Locators.purpose_optn)).click()
    def remarks_to(self,remarks):
        remarks_is=self.wait.until(EC.presence_of_element_located(Inputdetails_Locators.remarks_xpath))
        assert (remarks_is.get_attribute("type")=="text"),"Input text in the remarks field."
        remarks_is.send_keys(remarks)
    def send_to(self):
        send_next=self.wait.until(EC.presence_of_element_located(Inputdetails_Locators.send_money_Xpath))
        assert (send_next.text=="Send Money"),"Go to Send Money option name did not matched"
        send_next.click()

