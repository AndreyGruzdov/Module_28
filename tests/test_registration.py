from pages.auth_page import AuthPage
from config import first_name, last_mame, valid_password, valid_email
def test_new_user_registration(web_browser):
    """Проверка страницы регистраци"""
    page = AuthPage(web_browser)
    page.register_field.click()
    assert 'b2c.passport.rt.ru/auth/realms/b2c/login-actions' in page.get_current_url()
    assert page.register_first.is_presented()
    assert page.register_last.is_presented()
    assert page.register_email.is_presented()
    assert page.register_now_passw.is_presented()
    assert page.register_passw_confirm.is_presented()
    assert page.register_region.is_presented()
    assert page.register_user_agreement.is_presented()
    assert page.register_logo.is_presented()
    assert page.register_left.is_presented()
    assert page.register_right.is_presented()

def test_register_existing_user(web_browser):
    """Повторная регистраци"""
    page = AuthPage(web_browser)
    page.register_field.click()
    page.register_first.send_keys(first_name)
    page.register_last.send_keys(last_mame)
    page.register_email.send_keys(valid_email)
    page.register_now_passw.send_keys(valid_password)
    page.register_passw_confirm.send_keys(valid_password)
    page.register_button.click()
    assert page.button_re_entry.is_presented()
    page.button_re_entry.click()
    assert 'https://b2c.passport.rt.ru/' in page.get_current_url()


