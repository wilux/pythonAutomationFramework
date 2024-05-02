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


def select_browser(browser_name, headless):

    if not browser_name:
        browser_name = 'firefox'
    if not headless:
        headless = False
    if browser_name == 'firefox':
        driver = create_firefox_driver(headless)
    elif browser_name == "chrome":
        driver = create_chrome_driver(headless)
    elif browser_name == "edge":
        driver = create_edge_driver(headless)
    elif browser_name == "opera":
        driver = create_opera_driver(headless)
    else:
        raise NotImplementedError('Browser not supported')
    return driver


def create_firefox_driver(headless):
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.implicitly_wait(TIME_OUT)
    return driver


def create_opera_driver(headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    options.add_experimental_option('w3c', True)
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=ChromiumService(OperaDriverManager().install()), options=options)
    driver.implicitly_wait(TIME_OUT)
    return driver


def create_chrome_driver(headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(TIME_OUT)
    return driver


def create_edge_driver(headless=False):
    options = webdriver.EdgeOptions()
    if headless:
        options.add_argument("--headless")

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    driver.implicitly_wait(TIME_OUT)
    return driver
