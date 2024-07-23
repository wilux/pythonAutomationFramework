from appium.webdriver.common.appiumby import AppiumBy


class HomeLocators(object):

    SLOGAN = {
        "android": [AppiumBy.XPATH, '//android.widget.TextView[@text="Demo app for the appium-boilerplate"]'],
        "ios": [AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Demo app for the appium-boilerplate"]']
    }
