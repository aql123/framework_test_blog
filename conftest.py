import pytest
import requests

@pytest.fixture()
def get_access_token1():
    get_url = 'https://api.weixin.qq.com/cgi-bin/token'
    params = {'grant_type': 'client_credential',
              'appid': 'wx87c7bed6cfa3308a',
              'secret': '93a85c7b4d021f3fad7a85bca4d0335d'
              }

    res = requests.get(url=get_url, params=params)
    # print(res.json())
    return res.json()['access_token']
