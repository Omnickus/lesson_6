
class El_main_page:
    """
    Элементы на главной странице
    """
    featured = [ # элементы популярных товаров на главной странице
        ("//*[@id='content']/div[2]/div[1]/div/div[2]/h4/a"), # Первая карточка
        ("//*[@id='content']/div[2]/div[2]/div/div[2]/h4/a"), # Вторая карточка
        ("//*[@id='content']/div[2]/div[3]/div/div[2]/h4/a"), # Третья карточка
        ("//*[@id='content']/div[2]/div[4]/div/div[2]/h4/a"), # Четвёртая карточка
    ]

class El_catalog:
    """
    Элементы каталог
    """
    common_url = {
        ('/desktops'),
        ('/laptop-notebook'),
        ('/component/monitor'),
        ('/tablet'),
        ('/smartphone'),
        ('/camera'),
        ('/mp3-players'),
    }
    common_elements = { # элементы desktops/camera
        'элементы_сеткой' : '//*[@id="list-view"]', # Показывать элементы сеткой 
        'элементы_списком' : '//*[@id="list-view"]', # Показывать элементы списком 
        'сортирвка_товара' : '//*[@id="input-sort"]', # сортировка товара 
        'количество_товаров_на_странице' : '//*[@id="input-limit"]', # Количество элементов на странице для отображения 
    }
