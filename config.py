valid_email = 'andrej169@yandex.ru'
valid_password = 'K42mbNVrZBgCsyA'
valid_telephone = '+79522840568'
no_valid_telephone = '+7*522840568'
url_rostelecom = 'https://b2c.passport.rt.ru/'
url_cod = 'https://my.rt.ru/'
url_email = "https://www.1secmail.com/api/v1/"

import random

engl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
domens = ['com','ua','ru','net']


def pass_gener():
    passw_random = ''
    for x in range(6):
        passw_random = ''.join([passw_random,random.choice(list(engl))])

    return passw_random.lower()


def email_gener():
    name_email = ''
    name_server = ''
    for x in range(6):
        name_email = ''.join([name_email,random.choice(engl)])
    for y in range(4):
        name_server = ''.join([name_server,random.choice(engl)])

    def domen():
        dom = random.choice(domens)
        return dom

    email = ''.join([name_email,'@',name_server,'.',domen()])
    return email.lower()


fcv = ''
for x in range(6):
    fcv = fcv + random.choice(list(engl))

login_no_valid = fcv
ls_no_valid = fcv

if __name__  == '__main__':
    pass
