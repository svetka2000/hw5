import json


class ColorizeMixin:
    repr_color_code=32
    print(f"\32[32m{repr_color_code}")

class Advert(ColorizeMixin):
    repr_color_code = 32# greendef
    def __init__(self, input_dict):
        self.price=0
        for i in input_dict.keys():
            if isinstance(input_dict[i], dict):
                self.__dict__[i]=Advert(input_dict[i])
            else:                
                self.__dict__[i] = input_dict[i]
    def __call__(cls, **kwargs):
        instance = cls.__new__(**kwargs)
        instance.__init__(**kwargs)
        return instance
    def __repr__ (self):
        return f'{self.title}|{self.price}₽'




if __name__ == '__main__':
    
    # создаем экземпляр класса Advert из JSON
    lesson_str = """{ "title": "python", "price": 0, "location": { "address": "город Москва, Лесная, 7", "metro_stations": ["Белорусская"] } }"""
    lesson = json.loads(lesson_str) 
    # обращаемся к атрибуту location.address
    lesson_ad=Advert(lesson)
    print(lesson_ad.location.metro_stations)
    lesson1_str="""{
    "title": "Вельш-корги",
    "price": 1000,
    "class_": "dogs",
    "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
    }"""
    lesson1 = json.loads(lesson1_str) 
    lesson_ad1=Advert(lesson1)
    print(lesson_ad1.price)

    lesson_str ='{"title": "iPhone X", "price": "100"}'
    lesson = json.loads(lesson_str) 
    lesson_ad = Advert(lesson)
    print(lesson_ad)
