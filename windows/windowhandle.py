import undetected_chromedriver as uc
# driver = uc.Chrome()
class WindowHandle:
    def __init__(self,driver):
        self.driver=driver
    def switch_to_child(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    def switch_to_parent(self):
        self.driver.switch_to.window(self.driver.window_handles[0])