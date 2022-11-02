#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_registration.py
import time
from pages.auth_page import AuthPage
from config import valid_email, valid_password, pass_gener

def test_new_user_registration(web_browser):
    page = AuthPage(web_browser)
    page.register_field.click()

    assert page.register_left.is_presented()
    assert page.register_right.is_presented()
    assert 'b2c.passport.rt.ru/auth/realms/b2c/login-actions' in page.get_current_url()
    assert page.register_first.is_presented()
    assert page.register_last.is_presented()
    assert page.register_email.is_presented()
    assert page.register_now_passw.is_presented()
    assert page.register_passw_confirm.is_presented()
    assert page.register_region.is_presented()
    assert page.register_user_agreement.is_presented()
    assert page.register_logo.is_presented()
    page.register_first.send_keys('123')
    page.register_last.send_keys('321')
    page.register_email.send_keys()


    #

    # ActionChains(web_browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
    #
    # ActionChains(web_browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

    time.sleep(2)