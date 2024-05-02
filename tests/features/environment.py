from utils.browser_selector import select_browser


def before_all(context):
    browser = context.config.userdata.get('browser')
    headless = context.config.userdata.get('headless')
    context.driver = select_browser(browser, headless)


def after_all(context):
    context.driver.quit()
