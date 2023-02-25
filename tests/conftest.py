import pytest
import os
from playwright.sync_api import sync_playwright
from utilities.utilities import capabilities, run_on
from pages import homepage, accountpage, productpage
import subprocess
import urllib
import json


@pytest.fixture(name="browser")
def playwright_browser(): 
    print(run_on)
    if run_on == 'local':
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            yield browser
    
    if run_on == 'cloud':
        with sync_playwright() as playwright:
            playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
            capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion        
            lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(json.dumps(capabilities))
            browser = playwright.chromium.connect(lt_cdp_url)
            yield browser            

@pytest.fixture
def account_page(browser):
    page = browser.new_context().new_page()    
    account_page = accountpage.AccountPage(page)
    yield account_page

@pytest.fixture
def home_page(browser):
    page = browser.new_context().new_page()    
    home_page = homepage.HomePage(page)
    yield home_page

@pytest.fixture
def product_page(browser):
    page = browser.new_context().new_page()    
    product_page = productpage.ProductPage(page)
    yield product_page
