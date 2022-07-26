from src.base_page import Base_page
from src.constructor import Find_el
import random

class Currency(Base_page):

    """ Класс с работы с из енением валюты на странице """

    _url_page = '/'

    _but_currency = '//*[@id="form-currency"]/div/button'

    _change_currency = {
        'euro': '//*[@id="form-currency"]/div/ul/li[1]/button',
        'pound_sterling' : '//*[@id="form-currency"]/div/ul/li[2]/button',
        'dollar' : '//*[@id="form-currency"]/div/ul/li[3]/button'
    }

    def currency(self):
        self._browser.get(self._browser.url + self._url_page)
        el = Find_el(path = self._but_currency, browser = self._browser, time = 5).find_by_xpah
        el.click()

        el = Find_el(path = random.choice(list(self._change_currency.values())), browser = self._browser, time = 5).find_by_xpah
        el.click()


