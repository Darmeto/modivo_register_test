from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCEPT_POLICY = (By.CSS_SELECTOR, '#marketing-approvals .button-icon')
    LOGIN = (By.CSS_SELECTOR, '.control a:nth-child(1)')
    ACCOUNT_LOGIN_ICON = (By.CSS_SELECTOR, 'div.base-tooltip.account a[href$="/login"] > svg')
    ACCOUNT_ICON = (By.CSS_SELECTOR, 'div.base-tooltip.account a[href$="/customer"] > svg')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button.toggle.base-button.tertiary.normal')
