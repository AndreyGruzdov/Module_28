from pages.auth_page import AuthPage
from config import valid_email, valid_password, valid_pone, login_no_valid, ls_no_valid #,pass_gener, email_gener

def test_main_page_all_items(web_browser):
    """Проверка главной страницы"""
    page = AuthPage(web_browser)
    assert page.text_authorization.is_visible()
    assert page.text_personal_area.is_visible()
    assert page.email_input_form.is_visible()
    assert page.password_input_form.is_visible()
    assert page.tab_phone.is_visible()
    assert page.tab_email.is_visible()
    assert page.tab_login.is_visible()
    assert page.tab_ls.is_visible()
    assert 'https://b2c.passport.rt.ru/' in page.get_current_url()

def test_positive_authorisation_phone(web_browser):
    """Авторизация по номеру телефона и паролю"""
    page = AuthPage(web_browser)
    page.tab_phone.click()
    page.email_input_form.send_keys(valid_pone)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click() #Снимаем галочку с поля запомнить меня
    page.btn.click()
    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_positive_authorisation_email(web_browser):
    """Авторизация по email и паролю"""
    page = AuthPage(web_browser)
    page.tab_email.click()
    page.email_input_form.send_keys(valid_email)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()

def test_negative_authorization_login(web_browser):
    """Не удачная авторизация по логину и паролю"""
    page = AuthPage(web_browser)
    page.tab_login.click()
    page.email_input_form.send_keys(login_no_valid)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert page.forgot_password.is_visible()
    assert page.invalid_login_password.is_visible()

def test_negative_authorization_ls(web_browser):
    """Не удачная авторизация по лицевому счету и паролю"""
    page = AuthPage(web_browser)
    page.tab_ls.click()
    page.email_input_form.send_keys(ls_no_valid)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert page.forgot_password.is_visible()
    assert page.invalid_login_password.is_visible()

