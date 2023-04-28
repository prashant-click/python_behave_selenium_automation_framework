from features.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    edit_user_name = (By.NAME, "username")
    edit_password = (By.NAME, "password")
    button_login = (By.XPATH, "//button[contains(.,'Login')]")
    HRM_Logo = (By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img")
    def __init__(self, context):
        BasePage.__init__(self,context.driver)
        self.context = context


    def enter_credentials(self,username,password):
        super().enter_text(self.edit_user_name,username )
        super().enter_text(self.edit_password, password)

    def click_Login_button(self):
        super().click_element(self.button_login)

    def check_if_HRMLogoPresent(self):
        super().check_if_element_present(self.HRM_Logo)






