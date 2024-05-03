import allure
from allure_commons.types import AttachmentType
from utils.browser_selector import select_browser


def before_all(context):
    browser = context.config.userdata.get('browser')
    option = context.config.userdata.get('option')
    context.driver = select_browser(browser, option)


def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_step(context, step):
    if context.driver:
        allure.attach(context.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
