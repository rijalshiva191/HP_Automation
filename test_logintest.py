# from pages.loginpage import test_login_first

# from drivers.basepage import Basepage
# driver = Basepage.uc.Chrome()
# import pytest
# # @pytest.fixture()
# test_login_first(driver=driver)
# Import necessary modules
import pytest
from pages.loginpage_test import test_login_first
from drivers.basepage import Basepage

# Define a fixture to initialize the driver
@pytest.fixture
def driver():
    # Assuming `Basepage.uc.Chrome()` initializes your driver
    driver_instance = Basepage.uc.Chrome()
    yield driver_instance
    # Teardown code can be added here to clean up resources after the test

# Use the fixture in a test function
def test_login(driver):
    # Call the login function using the driver provided by the fixture
    test_login_first(driver=driver)
    # Add assertions or further test steps here
# assert driver.title == "Expected Title"  # Example assertion