from faker import Faker
from pages.main_page import MainPage
from pages.register_page import RegisterPage
import pytest


@pytest.mark.usefixtures("setup")
class TestRegisterPage:

    def test_register_page(self, setup):
        main_page = MainPage(self.driver)
        register_page = RegisterPage(self.driver)
        fake = Faker()
        main_page.open_page()
        main_page.accept_policy()
        main_page.register_btn()
        register_page.email(fake.email())
        register_page.password('Test123456!@')
        register_page.gender_choice()
        register_page.terms()
        register_page.create_account()