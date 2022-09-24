import json
from keyword import iskeyword


class ObjFromJSON:
    def __init__(self, data: dict[str, object]) -> None:
        for key, val in data.items():
            name = key + '_' if iskeyword(key) else key
            if isinstance(key, (list, tuple)):
                setattr(self, name, [ObjFromJSON(v) if isinstance(v, dict) else v for v in val])
            else:
                setattr(self, name, ObjFromJSON(val) if isinstance(val, dict) else val)


class ColorizeMixin:
    repr_color_code = 33

    def __repr__(self):
        return f'\033[1;{ColorizeMixin.repr_color_code};40m '


class Advert(ColorizeMixin, ObjFromJSON):
    def __init__(self, data: dict[str, object]):
        # initialization from dict
        # check if 'title' in fields
        if 'title' not in data.keys():
            raise KeyError('Title is a required field')

        try:
            if data['price'] < 0:
                raise ValueError('Price must be >= 0')
        except KeyError:
            data['price'] = 0

        super().__init__(data)

    def __repr__(self):
        return super().__repr__() + f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    ad1_str = """{
"title": "python", "class": "lesson",
"location": {
"address": "город Москва, Лесная, 7",
"metro_stations": ["Белорусская"]
}
}"""
    ad1 = json.loads(ad1_str)
    print(Advert(ad1))
    print(Advert(ad1).__dict__)

    ad2_str = """{
"title": "Вельш-корги",
"price": 1000,
"class": "dogs",
"location": {
"address": "сельское поселение Ельдигинское, поселок санатория
Тишково, 25"
}
}"""

    ad2 = json.loads(ad2_str, strict=False)
    print(Advert(ad2))

