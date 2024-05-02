from behave import step
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step("El usuario abre la pagina principal")
def step_impl(context):
    context.driver.get(context.env)


@step("El usuario verifica que el titulo de la pagina principal es correcto")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.title_contains("GlobalSQA"))
