from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

TIME_OUT = 5


def select_browser(browser_name, option):
    if option is None:
        option = "--"
    if not browser_name:
        browser_name = 'firefox'
    if browser_name == 'firefox':
        driver = create_firefox_driver(option)
    elif browser_name == "chrome":
        driver = create_chrome_driver(option)
    elif browser_name == "edge":
        driver = create_edge_driver(option)
    elif browser_name == "opera":
        driver = create_opera_driver(option)
    else:
        raise NotImplementedError('Browser not supported')
    driver.implicitly_wait(TIME_OUT)
    return driver


def create_firefox_driver(arguments):
    options = webdriver.FirefoxOptions()
    options.add_argument(arguments)
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    return driver


def create_opera_driver(arguments):
    options = webdriver.ChromeOptions()
    options.add_argument(arguments)
    options.add_experimental_option('w3c', True)
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=ChromiumService(OperaDriverManager().install()), options=options)
    return driver


def create_chrome_driver(arguments):
    options = webdriver.ChromeOptions()
    options.add_argument(arguments)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver


def create_edge_driver(arguments):
    options = webdriver.EdgeOptions()
    options.add_argument(arguments)
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    return driver
