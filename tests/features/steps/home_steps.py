from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step('The {actor} opens {url}')
def step_impl(context, actor, url):
    context.driver.get(url)


@step('Then {actor} sees "{text}" title')
def step_impl(context, actor, text):
    title_locator = (By.CSS_SELECTOR, ".post-2715 > div:nth-of-type(1) h2")
    title_element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(title_locator))
    assert title_element.text == "Automate Selenium/Protractor Automation  Scripts"

