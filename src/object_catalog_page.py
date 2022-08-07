from src.base.base_page import Base_page
from src.base.logger import Logger
from src.constructor import Find_el

class Catalog(Base_page):

    """ Класс с элементами разных категорий """

    common_url = {
        ('/desktops'),
        ('/laptop-notebook'),
        ('/component/monitor'),
        ('/tablet'),
        ('/smartphone'),
        ('/camera'),
        ('/mp3-players'),
    }
    common_elements = {
        'элементы_сеткой' : '//*[@id="list-view"]', # Показывать элементы сеткой 
        'элементы_списком' : '//*[@id="list-view"]', # Показывать элементы списком 
        'сортирвка_товара' : '//*[@id="input-sort"]', # сортировка товара 
        'количество_товаров_на_странице' : '//*[@id="input-limit"]', # Количество элементов на странице для отображения 
    }

    def catalog(self, url):
        self._browser.get(self._browser.url + url)
        Logger(f'Открыл страницу - {self._browser.url + url}').infolog
        Find_el(path = self.common_elements['элементы_сеткой'], browser = self._browser, time = 5).find_by_xpah
        Find_el(path = self.common_elements['элементы_списком'], browser = self._browser, time = 5).find_by_xpah
        Find_el(path = self.common_elements['сортирвка_товара'], browser = self._browser, time = 5).find_by_xpah
        Find_el(path = self.common_elements['количество_товаров_на_странице'], browser = self._browser, time = 5).find_by_xpah
        Logger(f'Все общие элементы присутствуют - {self._browser.url + url}').infolog

