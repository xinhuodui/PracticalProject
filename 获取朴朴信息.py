import json
from time import strftime, sleep

import requests


def request_url():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/dde2c9bc-61fd-41e6-b7fb-6cd3ca559f6d'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    res = requests.get(url, headers=head)
    dict1 = json.loads(res.text)
    name = dict1["data"]["name"]  # 商品名字
    spec = dict1["data"]["spec"]  # 规格
    price = str(int(dict1["data"]["price"]) / 100)  # 折扣价
    market_price = str(int(dict1["data"]["market_price"]) / 100)  # 原价
    share_content = dict1["data"]["share_content"]  # 详细内容
    print("-------------商品：" + name + "-------------")
    print("规格：" + spec)
    print("原价：" + price)
    print("原价/折扣价：" + price + "/" + market_price)

