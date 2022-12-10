import json

import requests


class RozetkaAPI:
    def __init__(self, item_id=0):
        self.item_id = item_id

    @staticmethod
    def get_item_data(current_id):
        dict_of_item = {}
        responce = requests.get(
            f'https://rozetka.com.ua/api/product-api/v4/goods/get-main?\
            front-type=xl&country=UA&lang=ua&goodsId={current_id}')
        if responce.status_code == requests.codes.ok:
            responce = json.loads(responce.text)
            dict_of_item['item_id'] = responce['data']['id']
            dict_of_item['title'] = responce['data']['title']
            dict_of_item['price'] = int(responce['data']['price'])
            dict_of_item['old_price'] = int(responce['data']['old_price'])
            dict_of_item['href'] = responce['data']['href']
            dict_of_item['brand'] = responce['data']['brand']
            dict_of_item['category'] = responce['data']['last_category']['title']
        else:
            dict_of_item = {'item_id': current_id,
                            'title': '',
                            'price': 0,
                            'old_price': 0,
                            'href': '',
                            'brand': '',
                            'category': ''}
        return dict_of_item


if __name__ == "__main__":
    item = RozetkaAPI()
    print(item.get_item_data(3365089))
