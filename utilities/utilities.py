from playwright.sync_api import Page
from dotenv import load_dotenv
import os

load_dotenv('secrets.env')
platform = os.getenv('PLATFORM')
browser = os.getenv('BROWSER')
run_on = os.getenv("RUN_ON") or 'local'

def set_test_status(page: Page, status: str, remark: str):
    """
    Function to set stats, title and description of test run on cloud grid
    :param page: instance of Playwright browser page
    :param status: status of test e.g Pass or Failed
    :param remark: additional remark about test status
    """
    page.evaluate(
        "_ => {}",
        "lambdatest_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}"
        )
    



capabilities = {
    'browserName': browser,
    'browserVersion': 'latest',
    'LT:Options': {
        'platform': platform,
        'build': 'Playwright Docker Demo Build',
        'name': f'Playwright Docker Test For {platform} & {browser}',
        'user': os.getenv('LT_USERNAME'),
        'accessKey': os.getenv('LT_ACCESS_KEY'),
        'network': True,
        'video': True,
        'visual': True,
        'console': True,
        'tunnel': False,   # Add tunnel configuration if testing locally hosted webpage
        'tunnelName': '',  # Optional
        'geoLocation': '', # country code can be fetched from https://www.lambdatest.com/capabilities-generator/
    }
}