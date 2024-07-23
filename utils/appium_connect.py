from requests import get as request_get, delete, exceptions
from appium import webdriver

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'
TIME_OUT = 1


def connect_to_appium(context, options):
    if get_appium_version() < 2:
        appium_path = '/wd/hub'
    else:
        appium_path = ''
    url = f'http://{APPIUM_HOST}:{APPIUM_PORT}{appium_path}'
    delete_previous_sessions(url)
    try:
        driver = webdriver.Remote(url, options=options)
    except Exception:
        raise ConnectionError
    driver.implicitly_wait(TIME_OUT)
    return driver


def get_appium_version():
    appium_1 = request_get('http://127.0.0.1:4723/wd/hub/status')
    appium_2 = request_get('http://127.0.0.1:4723/status')

    if appium_1.status_code == 200:
        data = appium_1.json()
        data = data.get("value", {}).get("build", {}).get("version")
        version = float(data[:-2])
        return version
    elif appium_2.status_code == 200:
        data = appium_2.json()
        data = data.get("value", {}).get("build", {}).get("version")
        version = float(data[:-2])
        return version
    else:
        assert False, "Error getting Appium version"


def get_appium_path():
    if get_appium_version() < 2:
        return '/wd/hub'
    else:
        return ''


def delete_previous_sessions(url):
    print("Deleting previous sessions...")
    sessions_url = f'{url}/sessions'
    session_url = f'{url}/session'
    try:
        response = request_get(sessions_url)
        response.raise_for_status()

        sessions_data = response.json()
        if not sessions_data["value"]:
            print("No active Appium sessions found.")
            return

        for session in sessions_data["value"]:
            session_id = session["id"]
            delete_url = f"{session_url}/{session_id}"
            delete_response = delete(delete_url)
            delete_response.raise_for_status()
            print(f"Session {session_id} deleted successfully.")

    except exceptions.RequestException as e:
        print(f"Error deleting sessions: {e}")
