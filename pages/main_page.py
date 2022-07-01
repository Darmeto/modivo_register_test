import locators.modivo_main_page_locators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.accept_policy_btn = locators.modivo_main_page_locators.MainPageLocators.ACCEPT_POLICY
        self.nav_to_register = locators.modivo_main_page_locators.MainPageLocators.REGISTRATION_BUTTON

    def open_page(self):
        self.driver.get('https://modivo.pl/login')

    def accept_policy(self):
        self.driver.find_element(*self.accept_policy_btn).click()

    def register_btn(self):
        self.driver.find_element(*self.nav_to_register).click()
