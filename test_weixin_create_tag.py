import requests
import pytest
import yaml
import allure

@pytest.mark.parametrize('create',
            yaml.safe_load(open('test_data.yaml','r',encoding='utf8')))
def test_create_tag(get_access_token1,create):
    url = create['url']+get_access_token1
    json_data = create['data']
    result=create['result']['name']
    res=requests.post(url,json=json_data)
    assert res.status_code==200
    assert res.json()['tag']['name']==result