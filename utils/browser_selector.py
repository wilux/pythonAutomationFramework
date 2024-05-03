from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


TIME_OUT = 5


def select_browser(browser_name, options):

    if not browser_name:
        browser_name = 'firefox'
    else:
        browser_name = browser_name.lower()

    if browser_name == 'firefox':
        driver = create_firefox_driver(options)
    elif browser_name == "chrome":
        driver = create_chrome_driver(options)
    elif browser_name == "edge":
        driver = create_edge_driver(options)
    elif browser_name == "opera":
        driver = create_opera_driver(options)
    else:
        raise NotImplementedError('Browser is not supported')
    driver.implicitly_wait(TIME_OUT)
    return driver


def add_personal_arguments(options, arguments):
    if arguments and arguments[0] != '':
        for argument in arguments:
            options.add_argument(argument)


def create_firefox_driver(arguments):
    options = webdriver.FirefoxOptions()
    add_personal_arguments(options, arguments)
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    return driver


def create_opera_driver(arguments):
    options = webdriver.ChromeOptions()
    add_personal_arguments(options, arguments)
    options.add_experimental_option('w3c', True)
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=ChromeService(OperaDriverManager().install()), options=options)
    return driver


def create_chrome_driver(arguments):
    options = webdriver.ChromeOptions()
    add_personal_arguments(options, arguments)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver


def create_edge_driver(arguments):
    options = webdriver.EdgeOptions()
    add_personal_arguments(options, arguments)
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    return driver
