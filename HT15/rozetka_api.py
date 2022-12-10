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
    def title(self):
        return self._title

    @title.setter
    def title(self, responce):
        self._title = responce

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, responce):
        self._price = responce

    @property
    def old_price(self):
        return self._old_price

    @old_price.setter
    def old_price(self, responce):
        self._old_price = responce

    @property
    def href(self):
        return self._href

    @href.setter
    def href(self, responce):
        self._href = responce

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, responce):
        self._brand = responce

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, responce):
        self._category = responce

    def get_item_data(self, item_id):
        responce = requests.get(
            f'https://rozetka.com.ua/api/product-api/v4/goods/get-main?\
            front-type=xl&country=UA&lang=ua&goodsId={item_id}')
        if responce.status_code == requests.codes.ok:
            responce = json.loads(responce.text)
            self.item_id = responce['data']['id']
            self.title = responce['data']['title']
            self.price = responce['data']['price']
            self.old_price = responce['data']['old_price']
            self.href = responce['data']['href']
            self.brand = responce['data']['brand']
            self.category = responce['data']['last_category']['title']
            return asdict(self)
        else:
            return dict(zip(['item_id', 'title', 'price', 'old_price', 'href', 'brand', 'category'],
                            [self.item_id, '', '', 0, '', '', '']))


if __name__ == "__main__":
    item = RozetkaAPI()
    print(item.get_item_data(item_id=336000))
