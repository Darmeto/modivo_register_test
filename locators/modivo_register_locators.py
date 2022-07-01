from selenium.webdriver.common.by import By


class RegisterLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register-modal')
    SOCIAL_MEDIA_SECTION = (By.CSS_SELECTOR, '.customer-social-login-wrapper')
    EMAIL = (By.CSS_SELECTOR, 'input[data-test-id=email-register]')
    REGISTRATION_EMAIL_ERROR = (By.CSS_SELECTOR, ' div[role="group"] div.field:nth-child(1) '
                                                 'div.error > span.error-msg')
    PASSWORD = (By.CSS_SELECTOR, 'input[data-test-id=password-register]')
    PASSWORD_ERROR = (By.CSS_SELECTOR, ' div[role="group"] div.field:nth-child(2) div.error > span.error-msg')
    CONFIRMATION = (By.CSS_SELECTOR, 'input[data-test-id=confirm]')
    CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, ' div[role="group"] div.field:nth-child(3) '
                                               'div.error > span.error-msg')
    GENDER_SELECT = (By.CSS_SELECTOR, 'div[class="dropdown field big"]')
    GENDER_OPTION = (By.CSS_SELECTOR, 'div.options-container li')
    MFC_CHECKBOX = (By.CSS_SELECTOR, 'label[for="loyalty_club_register"] svg')
    NEWSLETTER_CHECKBOX = (By.CSS_SELECTOR, 'label[for="is_subscribed"]')
    TERMS_CHECKBOX = (By.CSS_SELECTOR, 'label[for="terms"] span')
    TERMS_ERROR = (By.CSS_SELECTOR, '.checkbox div .error-msg')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[data-test-id=create-account-button]')
    register_message_pass = (By.LINK_TEXT, 'Udana rejestracja.')