from cgi import test
from src.base_page import Base_page
from src.constructor import Find_el
from src.constructor import Placeholder
from src.constructor import Actions

import time


class Admin_page(Base_page):

    """ Класс с элементами стриницы администратора """

    admin_login = 'user'
    admin_password = 'bitnami'
    but_login = '//*[@id="content"]/div/div/div/div/div[2]/form/div[3]/button'

    id_user_name = "input-username"
    name_password = "password"
    sel_submit = "button[type='submit']"
    text_forgoted_password= "Forgotten Password"
    xpath_open_cart = "//*[text()='OpenCart']"

    catalog = '//*[@id="menu-catalog"]/a'
    success_del = 'Success: You have modified products!'

    def enter_admin(self):
        self._browser.get(self._browser.url + "/admin")

        el = Find_el(path = self.id_user_name, browser = self._browser, time = 5).find_by_id
        el.click()
        Placeholder(browser = self._browser, el = el, text = self.admin_login).char_by_char()

        el = Find_el(path = self.name_password, browser = self._browser, time = 5).find_by_name
        el.click()
        Placeholder(browser = self._browser, el = el, text = self.admin_password).char_by_char()

        # Нажать логин в админку
        el = Find_el(path= self.but_login, browser= self._browser, time = 7).find_by_xpah
        el.click()
    


    def admin_page(self):
        self._browser.get(self._browser.url + "/admin")
        Find_el(path = self.id_user_name, browser = self._browser, time = 5).find_by_id
        Find_el(path = self.name_password, browser = self._browser, time = 5).find_by_name
        Find_el(path = self.sel_submit, browser = self._browser, time = 5).find_by_selector
        Find_el(path = self.text_forgoted_password, browser = self._browser, time = 5).find_by_link_text
        Find_el(path = self.xpath_open_cart, browser = self._browser, time = 5).find_by_xpah

    def add_new_item(self):
        # Вход в админку
        self.enter_admin()

        # Нажать на категории
        el = Find_el(path = self.catalog, browser = self._browser, time = 10).find_by_xpah
        Actions(browser=self._browser, el = el).click()
        time.sleep(2)

        # Нажать на продукты
        el = Find_el(path = '//*[@id="collapse1"]/li[2]/a', browser=self._browser, time=7).find_by_xpah
        Actions(browser=self._browser, el = el).click()

        # Нажать добавить товар
        el = Find_el(path='//*[@id="content"]/div[1]/div/div/a', browser=self._browser, time=10).find_by_xpah
        el.click()

        # Плэйсхолдер имя продукты
        el = Find_el(path = '//*[@id="input-name1"]', browser=self._browser, time=15).find_by_xpah
        el.click()
        Placeholder(browser=self._browser, el = el, text = 'Super item').char_by_char()

        # Плэйсхолдер описания товара
        el = Find_el(path = '//*[@id="language1"]/div[2]/div/div/div[3]/div[2]', browser=self._browser, time=5).find_by_xpah
        Actions(browser=self._browser, el = el).click()
        Placeholder(browser=self._browser, el=el, text='Super description for item').char_by_char()

        # Мета таг
        el = Find_el(path = '//*[@id="input-meta-title1"]', browser=self._browser, time=5).find_by_xpah
        el.click()
        Placeholder(browser=self._browser, el=el, text='MetaTag').char_by_char()

        # Переход на вкладку Data
        el = Find_el(path='//*[@id="form-product"]/ul/li[2]/a', browser=self._browser, time=5).find_by_xpah
        el.click()

        # Плэйсхолдер модели
        el = Find_el(path = '//*[@id="input-model"]', browser=self._browser, time=10).find_by_xpah
        el.click()
        Placeholder(browser=self._browser, el=el, text = 'Samsung').char_by_char()

        # Сохранить новый товар
        el = Find_el(path = '//*[@id="content"]/div[1]/div/div/button', browser=self._browser, time = 10).find_by_xpah
        el.click()



    def del_item(self):
        # Вход в админку
        self.enter_admin()

        # Нажать на категории
        el = Find_el(path = self.catalog, browser = self._browser, time = 10).find_by_xpah
        Actions(browser=self._browser, el = el).click()
        time.sleep(2)

        # Нажать на продукты
        el = Find_el(path = '//*[@id="collapse1"]/li[2]/a', browser=self._browser, time=7).find_by_xpah
        Actions(browser=self._browser, el = el).click()

        # Выбор фальтра по имени
        el = Find_el(path = '//*[@id="input-name"]', browser=self._browser, time=5).find_by_xpah
        el.click()
        Placeholder(browser=self._browser, el = el , text = 'Super item').char_by_char()

        # Клик по кнопке отфильтровать
        el = Find_el(path = '//*[@id="button-filter"]', browser=self._browser, time=10).find_by_xpah
        el.click()

        # Удаление товара (Предполагаю, что при поиске по имени будет найден один элемент, если больше то ошибка)
        el = Find_el(path = '//*[@id="form-product"]/div/table/tbody', browser=self._browser, time = 10).find_by_xpah
        child = el.find_elements_by_css_selector('tr')
        if len(child) != 1:
            assert len(child) == 1

        # Выбираю товал для удаления
        el = child[0].find_element_by_css_selector('input')
        el.click()

        # Удаляю выбранный товар
        el = Find_el(path='//*[@id="content"]/div[1]/div/div/button[3]', browser=self._browser, time=10).find_by_xpah
        el.click()
        self._browser.switch_to.alert.accept()

        # Проверяю, что появилось сообщение с успешным удалением
        el = Find_el(path = '//*[@id="content"]/div[2]/div[1]/i', browser=self._browser, time=15).find_by_xpah

