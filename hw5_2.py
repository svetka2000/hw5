import json
import keyword
from typing import Dict

class ColorizeMixin:
    """
    меняет цвет теĸста при выводе на ĸонсоль\n
    задает цвет в атрибуте ĸласса repr_color_code
    """
    repr_color_code = 32  # green
    def __repr__(self):
        return f'\033[1;{self.repr_color_code};40m{self.title}|{self.price_}₽'


class InnerAdvert():
    """
    динамичесĸи создает атрибуты эĸземпляра класса для полей класса Advert (например location) 
    """
    def __init__(self, input_dict: Dict):
        for key, value in input_dict.items():
            if isinstance(value, dict):
                self.__dict__[key] = InnerAdvert(value)
            elif key in keyword.kwlist:
                self.__dict__[f'{key}_'] = value
            else:
                self.__dict__[key] = value


class Advert(ColorizeMixin):
    """
    динамичесĸи создает атрибуты эĸземпляра ĸласса из атрибутов JSON-объеĸта\n
    title - обязательное поле\n
    обращаться ĸ атрибутам можно через точĸу
    """
    repr_color_code = 33  # yellow

    def __init__(self, input_dict: Dict):
        price_existence = 0
        if 'title' not in input_dict:
            raise ValueError
        for key, value in input_dict.items():
            if isinstance(value, dict):
                self.__dict__[key] = InnerAdvert(value)
            elif key in keyword.kwlist:
                self.__dict__[f'{key}_'] = value
            elif key == 'price':
                price_existence = 1
                if value >= 0:
                    self.__dict__['price_'] = value
                else:
                    raise ValueError
            else:
                self.__dict__[key] = value
        if not price_existence:
            self.__dict__['price_'] = 0

    @property
    def price(self):
        return self.price_

    def __repr__(self):
        """
        выводит название и цену объявления
        """
        return super().__repr__()


if __name__ == '__main__':
    # создаем экземпляр класса Advert из JSON
    lesson_str = """{ 
                        "title": "python", 
                        "price": 0, 
                        "location": 
                            { 
                            "address": "город Москва, Лесная, 7", 
                            "metro_stations": ["Белорусская"] 
                            } 
                    }"""
    lesson = json.loads(lesson_str)
    # обращаемся к атрибуту location.address
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    corgi = """{
                        "title": "Вельш-корги",
                        "price": 1000,
                        "class": "dogs",
                        "location": {
                        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                        }
                    }"""
    corgi = json.loads(corgi)
    corgi_ad = Advert(corgi)
    print(corgi_ad.price)
    print(corgi_ad.class_)

    lesson1_str = '{"title": "iPhone X", "price": -10}'
    lesson1 = json.loads(lesson1_str)
    lesson1_ad = Advert(lesson1)
    print(lesson1_ad)

    lesson_str = '{"title": "iPhone X"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)

    

