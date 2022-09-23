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
    def __repr__(self):
        print(1)


class Advert(ColorizeMixin, ObjFromJSON):
    def __init__(self, data: dict[str, object]):
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
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    print(Advert(json.loads("""{
    "title": "python", "price": 0,
    "class": "d",
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }""")))
    print(Advert.mro())