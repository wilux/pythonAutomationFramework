import allure
from allure_commons.types import AttachmentType
from utils.browser_selector import select_browser


def before_all(context):
    browser = context.config.userdata.get('browser')
    options = context.config.userdata.get("options", "").split(",")
    context.driver = select_browser(browser, options)


def after_all(context):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()


def after_step(context, step):
    if hasattr(context, 'driver') and context.driver:
        # if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
