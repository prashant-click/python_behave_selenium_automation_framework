from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import  WebDriverWait



class BasePage:

    def __init__(self,driver):
        self.driver = driver


    def enter_text(self,by_locator,input_text):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(input_text)
        except Exception as e:
            print(f"Unable to enter text because of  {e}")

    def click_element(self,by_locator):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click()
        except Exception as e:
            print(f"Unable to click element because of  {e}")

    def check_if_element_present(self,by_locator):
        print("inside element present")
        assert WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator)).is_displayed()

