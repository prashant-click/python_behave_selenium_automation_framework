import configparser
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path
from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from datetime import datetime

root = Path(__file__).parents[1]

def before_scenario(context,scenario):

    config_file_path = Path.joinpath(root, "configuration", "config.ini")
    print(config_file_path)
    context.conf = configparser.ConfigParser()
    context.conf.read(config_file_path)
    browser = context.conf['ENVIRONMENT']['browser']
    url = context.conf['ENVIRONMENT']['url']
    print(f" Browser {browser} will be used in the execution")
    if (browser.lower()=="chrome"):
        print("before_scenario")
        ops = webdriver.ChromeOptions()
        ops.add_argument("--start-maximized")
        driver_path = str(Path.joinpath(root, "drivers", "chromedriver.exe"))
        serv_obj = Service(driver_path)
        context.driver = webdriver.Chrome(service=serv_obj, options=ops)
        basepage = BasePage(context.driver)
        context.LoginPage =LoginPage(basepage)
        context.driver.get(url)
def after_step(context,step):
    current_time = datetime.now()
    time_stamp = current_time.timestamp()
    attach(context.driver.get_screenshot_as_png(),name=time_stamp,attachment_type=AttachmentType.PNG)

def after_scenario(context, scenario):
    context.driver.close()