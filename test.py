import requests
import json
import re

HEADERS = {
  "DeviceId": "4C5E07D1-E418-47B1-A29E-662DE191BE8B",
  "X-Retail-Brand": "lo",
  "X-Platform": "omniapp",
  "SessionToken": "183D76877F848E43D6553B4A351286EE"
}

data = {
    "limit": 5,
    "offset": 0,
}

region_data = {
      "jsonrpc": "2.0",
      "params": {
        "type": "pickup",
        "storeId": 4069  # 4069 - Москва, 3139 - Санкт-Петербург
      },
      "id": 1,
      "method": "deliveryModeSet"
}

auth_data = {
  "id": 1,
  "jsonrpc": "2.0",
  "method": "deliveryModeGet"
}

# res = requests.post(headers=HEADERS, url='https://lentochka.lenta.com/jrpc/deliveryModeSet', json=region_data)
# print(res.status_code)

res = requests.post(headers=HEADERS, url='https://lentochka.lenta.com/jrpc/deliveryModeGet', json=auth_data)
print(res.status_code)
print(res.text)

# response = requests.post(headers=HEADERS, url='https://api.lenta.com/v1/catalog/items', json=data)
#
# data = response.json()
# del data['categories']
# del data['filters']
#
# for item in data['items']:
#     print(json.dumps(item, indent=4, ensure_ascii=False))
#     brand = re.search(r'(?<=[\s^])[A-ZА-Я\s]+(?=[$\s])', item['name'])
#     print(brand.group(0))
#     break
