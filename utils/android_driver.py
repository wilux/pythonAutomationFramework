from appium.options.android import UiAutomator2Options
from utils.appium_connect import connect_to_appium


def create_android_driver(context):
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'appActivity': "MainActivity",
        'appPackage': "com.wdiodemoapp",
    })
    yield connect_to_appium(context, options)
