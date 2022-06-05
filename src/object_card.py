from src.base_page import Base_page
from src.constructor import Find_el

class Card(Base_page):

    """ Класс с элементами карточек товара """

    featured = [ # элементы популярных товаров на главной странице
        ("//*[@id='content']/div[2]/div[1]/div/div[2]/h4/a"), # Первая карточка
        ("//*[@id='content']/div[2]/div[2]/div/div[2]/h4/a"), # Вторая карточка
        ("//*[@id='content']/div[2]/div[3]/div/div[2]/h4/a"), # Третья карточка
        ("//*[@id='content']/div[2]/div[4]/div/div[2]/h4/a"), # Четвёртая карточка
    ]

    def card(self, path):
        Find_el(path = path, browser = self._browser, time = 5).find_by_xpah.click()
        Find_el(path = 'button-cart', browser = self._browser, time = 5).find_by_id
        Find_el(path = 'Tweet', browser = self._browser, time = 5).find_by_link_text
        Find_el(path = 'Description', browser = self._browser, time = 5).find_by_link_text
        Find_el(path = '//*[contains(text(), "Reviews")]', browser = self._browser, time = 5).find_by_xpah