from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCEPT_POLICY = (By.CSS_SELECTOR, '#marketing-approvals .button-icon')
    LOGIN = (By.CSS_SELECTOR, '.control a:nth-child(1)')
