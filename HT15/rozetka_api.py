import json

from dataclasses import dataclass, asdict

import requests


@dataclass
class RozetkaAPI:
    item_id: int = 0
    title: str = ''
    price: int = 0
    old_price: int = 0
    href: str = ''
    brand: str = ''
    category: str = ''


    def get_item_data(self):
        responce = requests.get(
            f'https://rozetka.com.ua/api/product-api/v4/goods/get-main?\
            front-type=xl&country=UA&lang=ua&goodsId={self.item_id}')
        if responce.status_code == requests.codes.ok:
            responce = json.loads(responce.text)
            self.item_id = responce['data']['id']
            self.title = responce['data']['title']
            self.price = int(responce['data']['price'])
            self.old_price = int(responce['data']['old_price'])
            self.href = responce['data']['href']
            self.brand = responce['data']['brand']
            self.category = responce['data']['last_category']['title']
         
        return asdict(self)


if __name__ == "__main__":
    item = RozetkaAPI(item_id=3365089)
    print(item.get_item_data())
