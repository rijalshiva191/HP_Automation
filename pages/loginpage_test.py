from definitions.logindef import Login_HP
from config.usercredentials import UserCredentials
from windows.windowhandle import WindowHandle
import pytest
import time
# @pytest.fixture()
def test_login_first(driver):
    login=Login_HP(driver)
    login.open_page(UserCredentials.url)
    login.signin()
    WindowHandle(driver).switch_to_child()
    login.email_input(UserCredentials.email_address)
    login.next()
    login.password_input(UserCredentials.password)
    login.password_next()
    time.sleep
    WindowHandle(driver).switch_to_parent()
    # driver.switch_to.window(driver.window_handles[0])