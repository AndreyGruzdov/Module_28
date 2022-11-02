from pages.base import WebPage
from pages.elements import WebElement
from config import url_rostelecom


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = url_rostelecom
        super().__init__(web_driver, url)


    text_authorization = WebElement(xpath="(//*[contains(text(), 'Авторизация')])")
    text_personal_area = WebElement(xpath="(// *[contains(text(),'Личный кабинет')])[2]")
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_email = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    email_input_form = WebElement(xpath="// *[ @ id ='username']")
    password_input_form = WebElement(xpath="// *[ @ id ='password']")
    check_mark = WebElement(xpath="//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[3]/label[1]/span[2]/span[1]")
    btn = WebElement(id='kc-login')
    forgot_password = WebElement(xpath = "//*[@id='forgot_password']")
    invalid_login_password =WebElement(xpath = "//*[@id='page-right']/div/div/p")
    incorrect_text = WebElement(xpath=" //*[@id='page-right']/div/div/p")
    captcha_text = WebElement(xpath="// *[contains(text(), 'Символы')]")
    captcha = WebElement(xpath="//*[@id='captcha']")

    register_left = WebElement(id='page-left')
    register_right = WebElement(id='page-right')
    register_field = WebElement(xpath="// *[ @ id ='kc-register']")
    register_first = WebElement(name= 'firstName')
    register_last = WebElement(name= 'lastName')
    register_email = WebElement(id="address")
    register_now_passw = WebElement(name="password")
    register_passw_confirm = WebElement(name="password-confirm")
    register_button = WebElement(name="register")
    register_region = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]')
    register_user_agreement = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[5]/a[1]')
    register_logo = WebElement(class_name='main-header__logo-container')

    text_recovery = WebElement(xpath="(//*[@id='page-right']/div[1]/div[1]/h1[1])")
    button_continue = WebElement(xpath="//*[@id='reset']")
    button_back = WebElement(xpath="//*[@id='reset-back']")
    tab_phone_trait = WebElement(xpath="(//*[@id='t-btn-tab-phone']/span)")
    tab_email_trait = WebElement(xpath="(//*[@id='t-btn-tab-mail']/span)")
    text_invalid = WebElement(xpath="(//*[@id='page-right']/div/div/p[1])")

