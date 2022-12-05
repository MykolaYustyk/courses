import json

from dataclasses import dataclass, asdict

import requests


@dataclass
class RozetkaAPI:
    item_id: int = 0
    _title: str = ''
    _price: int = 0
    _old_price: int = 0
    _href: str = ''
    _brand: str = ''
    _category: str = ''

    @property
    def __title(self):
        return self._title

    @__title.setter
    def __title(self, responce):
        self._title = responce

    @property
    def __price(self):
        return self._price

    @__price.setter
    def __price(self, responce):
        self._price = responce

    @property
    def __old_price(self):
        return self._old_price

    @__old_price.setter
    def __old_price(self, responce):
        self._old_price = responce

    @property
    def __href(self):
        return self._href

    @__href.setter
    def __href(self, responce):
        self._href = responce

    @property
    def __brand(self):
        return self._brand

    @__brand.setter
    def __brand(self, responce):
        self._brand = responce

    @property
    def __category(self):
        return self._category

    @__category.setter
    def __category(self, responce):
        self._category = responce

    def get_item_data(self, item_id):
        responce = requests.get(
            f'https://rozetka.com.ua/api/product-api/v4/goods/get-main?\
            front-type=xl&country=UA&lang=ua&goodsId={item_id}')
        if responce.status_code == requests.codes.ok:
            responce = json.loads(responce.text)
            self.item_id = responce['data']['id']
            self.__title = responce['data']['title']
            self.__price = responce['data']['price']
            self.__old_price = responce['data']['old_price']
            self.__href = responce['data']['href']
            self.__brand = responce['data']['brand']
            self.__category = responce['data']['last_category']['title']
            return {key.strip('_'): value for key, value in asdict(self).items()}
        else:
            return dict(zip(['item_id', 'title', 'price', 'old_price','href', 'brand', 'category'],
                            [self.item_id, '', '', 0, '', '','']))


if __name__ == "__main__":
    item = RozetkaAPI()
    print(item.get_item_data(item_id=336000))
