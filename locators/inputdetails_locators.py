from selenium.webdriver.common.by import By
class Inputdetails_Locators:
        money_trnsfr=(By.XPATH,'//*[@id="app"]/div/main/div[4]/div/div[2]')
        # send_optn_path=(By.XPATH,"//*[@id='app']/div/div[26]/div[3]/div[1]")
        send_optn_path=(By.XPATH,"//*[@id='app']/div/div[26]/div[3]/div[1]/div/h3")
        receiver_phone_number=(By.XPATH,"//*[@id='phone']")
        amount_xpath=(By.XPATH,"//*[@id='phone_no']")
        purpose_xpath=(By.XPATH,"//*[@id='app']/div/div[28]/div[2]/div[3]/form/div[1]/div[3]/div/div/div")
        purpose_optn=(By.XPATH,"//*[@id='dropdown']/ul/li[2]/h3")
        remarks_xpath=(By.XPATH,"//*[@id='app']/div/div[28]/div[2]/div[3]/form/div[1]/div[4]/div/input")
        
        send_money_Xpath=(By.XPATH,'//*[@id="spinButton"]')

