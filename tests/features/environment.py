from utils.browser_selector import select_browser


def before_all(context):
    browser = context.config.userdata.get('browser')
    option = context.config.userdata.get('option')
    context.driver = select_browser(browser, option)


def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()
