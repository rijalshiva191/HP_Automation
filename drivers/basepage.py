class Basepage:
    from selenium.webdriver.chrome.options import Options
    import undetected_chromedriver as uc
    # from utils.windowhandle import WindowHandle

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)