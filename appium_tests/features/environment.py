from allure import attach
from allure_commons.types import AttachmentType
from behave import use_fixture
from utils.android_driver import create_android_driver
from utils.ios_driver import create_ios_driver

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


def before_scenario(context, scenario):
    tag_names = scenario.effective_tags
    device = "android"
    for tag_name in tag_names:
        tag_parts = tag_name.split("=")
        key = tag_parts[0].lower()
        if key == "ios":
            device = key
            context.udid = tag_parts[1] if len(tag_parts) > 1 else None
    if device.lower() == "ios":
        context.driver = use_fixture(create_ios_driver, context)
    else:
        context.driver = use_fixture(create_android_driver, context)


def after_step(context, step):
    if hasattr(context, "driver"):
        # if step.status == "failed":
        attach(context.driver.get_screenshot_as_png(), name='Screenshot',
               attachment_type=AttachmentType.PNG)
