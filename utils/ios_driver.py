from appium.options.ios import XCUITestOptions
from utils.appium_connect import connect_to_appium


def create_ios_driver(context):
    options = XCUITestOptions().load_capabilities({
        'platformName': 'iOS',
        'appium:automationName': 'XCUITest',
        'udid': context.udid,
        'bundleId': "org.reactjs.native.example.wdiodemoapp"
    })

    yield connect_to_appium(context, options)
