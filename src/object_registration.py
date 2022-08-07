from src.base.base_page import Base_page
from src.base.logger import Logger
from src.constructor import Find_el
from src.constructor import Placeholder


class Registration(Base_page):

    """ Класс для тестов на странице регистрации """

    my_acc = 'My Account'
    reg = 'Register'
    first_name = 'firstname'
    last_name = 'lastname'
    email = 'email'
    telephone = 'telephone'
    password = 'password'
    confirm = 'confirm'
    subscribe = '//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input'
    agree = 'agree'
    submit = '//*[@id="content"]/form/div/div/input[2]'

    def registration_user(self):
        el = Find_el(browser = self._browser, time=5, path = self.my_acc).find_by_link_text
        el.click()
        Logger(f'Кликнул на мой аккаунт').infolog

        el = Find_el(browser = self._browser, time=5, path = self.reg).find_by_link_text
        el.click()
        Logger(f'Кликнул на регистрацию').infolog

        el = Find_el(browser = self._browser, time=5, path = self.first_name).find_by_name
        el.click()
        Placeholder(browser = self._browser, el = el, text = 'Andrey').char_by_char()
        Logger(f'Ввёл имя').infolog

        el = Find_el(browser = self._browser, time=5, path = self.last_name).find_by_name
        el.click()
        Placeholder(browser = self._browser, el = el, text = 'Samuylov').char_by_char()
        Logger(f'Ввёл фамилию').infolog

        el = Find_el(browser = self._browser, time=5, path = self.email).find_by_name
        el.click()
        Placeholder(browser = self._browser, el = el, text = 'test@email.ru').char_by_char()
        Logger(f'Ввёл почту').infolog

        el = Find_el(browser = self._browser, time=5, path = self.telephone).find_by_name
        el.click()
        Placeholder(browser = self._browser, el = el, text = '89851111111').char_by_char()
        Logger(f'Ввёл номер телефона').infolog

        el = Find_el(browser = self._browser, time=5, path = self.password).find_by_name
        el.click()
        Placeholder(browser = self._browser, el = el, text = 'qwerty').char_by_char()
        Logger(f'Ввёл пароль').infolog

        el = Find_el(browser = self._browser, time=5, path = self.confirm).find_by_name
        el.click()
        Placeholder(browser = self._browser, el = el, text = 'qwerty').char_by_char()
        Logger(f'Повторил пароль').infolog

        el = Find_el(browser = self._browser, time=5, path = self.subscribe).find_by_xpah
        el.click()
        Logger(f'Кликнул на подписку').infolog

        el = Find_el(browser = self._browser, time=5, path = self.agree).find_by_name
        el.click()
        Logger(f'Кликнул на соглашение').infolog

        el = Find_el(browser = self._browser, time=5, path = self.submit).find_by_xpah
        el.click()
        Logger(f'Нажал подтвердить').infolog

