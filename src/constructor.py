from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time

class Find_el:

    """ Вспомогательный класс для работы с элементами DOM """

    def __init__(self, path = None, time = None, browser = None) -> None:
        self._path = path
        self._wtime = time
        self._browser = browser
        if self._wtime == None:
            self._wtime = 10
        
    @property
    def find_by_xpah(self):
        return WebDriverWait(self._browser, timeout=self._wtime).until(EC.presence_of_element_located((By.XPATH, self._path)))

    @property
    def find_by_id(self):
        return WebDriverWait(self._browser, timeout=self._wtime).until(EC.presence_of_element_located((By.ID, self._path)))

    @property
    def find_by_name(self):
        return WebDriverWait(self._browser, timeout=self._wtime).until(EC.presence_of_element_located((By.NAME, self._path)))
    
    @property
    def find_by_selector(self):
        return WebDriverWait(self._browser, timeout=self._wtime).until(EC.presence_of_element_located((By.CSS_SELECTOR, self._path)))

    @property
    def find_by_link_text(self):
        return WebDriverWait(self._browser, timeout=self._wtime).until(EC.presence_of_element_located((By.LINK_TEXT, self._path)))

    @property
    def finds_by_xpath(self):
        return self._browser.find_elements_by_xpath(self._path)


class Placeholder:

    """ Вспомогательный класс для работы с плэйсхолдорами, радиокнопками и тд """

    def __init__(self, browser, text = None, el = None) -> None:
        self._browser = browser
        self._text = text
        self._el = el

    def char_by_char(self):
        """ Посимвольный ввод текста """
        for i in self._text:
            self._el.send_keys(i)
            time.sleep(0.1)

class Actions:

    """ Вспомогательный класс для работы с цепочками действий """

    def __init__(self, browser, el) -> None:
        self._browser = browser
        self._el = el

    def click(self):
        action = ActionChains(self._browser)
        action.click(on_element = self._el)
        action.perform()
        action.reset_actions()

