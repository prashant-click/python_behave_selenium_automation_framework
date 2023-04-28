from behave import *
from pathlib import Path
import time



root = Path(__file__).parents[2]

@given('I enter the url')
def enter_url(context):
    # context.driver=driver
    pass


@when('I enter the username as "{username}" and password "{password}"')
def enter_credentials(context,username,password):
    try:
        context.LoginPage.enter_credentials(username,password)
        time.sleep(2)
    except :
        print("Exception Occured")




@when('click on login button')
def click_login_button(context):
    print("clicking login button")
    context.LoginPage.click_Login_button()

@then('I should see the OrangeHRM logo')
def verify_logo(context):
    context.LoginPage.check_if_HRMLogoPresent()

