import random

import locators.modivo_register_locators


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = locators.modivo_register_locators.RegisterLocators.EMAIL
        self.password_input = locators.modivo_register_locators.RegisterLocators.PASSWORD
        self.repeat_password_input = locators.modivo_register_locators.RegisterLocators.CONFIRMATION
        self.gender_choice_btn = locators.modivo_register_locators.RegisterLocators.GENDER_SELECT
        self.gender_option = locators.modivo_register_locators.RegisterLocators.GENDER_OPTION
        self.select_terms = locators.modivo_register_locators.RegisterLocators.TERMS_CHECKBOX
        self.submit_button = locators.modivo_register_locators.RegisterLocators.SUBMIT_BUTTON
        self.register_pass = locators.modivo_register_locators.RegisterLocators.register_message_pass

    def email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.repeat_password_input).send_keys(password)

    def gender_choice(self):
        self.driver.find_element(*self.gender_choice_btn).click()
        gender_op = self.driver.find_elements(*self.gender_option)
        chosen_gender = random.choice(gender_op)
        chosen_gender.click()

    def terms(self):
        self.driver.find_element(*self.select_terms).click()

    def create_account(self):
        self.driver.find_element(*self.submit_button).click()

    def reg_pass(self):
        return self.driver.find_element(*self.register_pass).is_displayed()
