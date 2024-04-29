from drivers.basepage import Basepage
import pytest
from pages.loginpage_test import test_login_first
from pages.userinputpage import test_input_details
from pages.usernextpage import test_buttons
# from utils.windowhandle import WindowHandle

driver = Basepage.uc.Chrome()


test_login_first(driver=driver)
test_input_details(driver=driver)
test_buttons(driver=driver)