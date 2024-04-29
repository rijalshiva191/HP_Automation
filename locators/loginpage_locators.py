from selenium.webdriver.common.by import By
class Loginpage_locators:
        signin_button=(By.XPATH, "//*[@id='app']/div/main/div[3]/div[1]/button")
        email_inputfield=(By.XPATH,"//*[@id='identifierId']")
        next_button=(By.XPATH,"//*[@id='identifierNext']/div/button/span")
        password_field=(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")
        password_nextbutton=(By.XPATH,"//*[@id='passwordNext']/div/button/span")