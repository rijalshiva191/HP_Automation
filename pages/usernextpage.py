import time
from definitions.usernextdef import Confirm_Pay_Tpin
import pytest
def test_buttons(driver):
    button=Confirm_Pay_Tpin(driver)
    button.confirm_button()
    button.pay_button()
    # time.sleep(10)
    button.tpin_field(" ")
    time.sleep(3)
    # button.done_button()