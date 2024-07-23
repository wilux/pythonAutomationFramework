from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium_tests.features.locators.home_locators import HomeLocators


@step('The {actor} sees "{text}" slogan')
def step_impl(context, actor, text):
    slogan_locator = (By.XPATH, '//android.widget.TextView[@text="Demo app for the appium-boilerplate"]')
    # slogan_locator = (By.XPATH, '//XCUIElementTypeStaticText[@name="Demo app for the appium-boilerplate"]')
    slogan_element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(slogan_locator))
    assert slogan_element.text == text

