from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step("El usuario abre la pagina DEMO de global SQA")
def step_impl(context):
    context.driver.get("https://www.globalsqa.com/demo-site/")


@step("El usuario ve el titulo Automate Selenium/Protractor Automation  Scripts")
def step_impl(context):
    title = (By.CSS_SELECTOR, ".post-2715 > div:nth-of-type(1) h2")
    title_element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(title))
    assert title_element.text == "Automate Selenium/Protractor Automation  Scripts"

