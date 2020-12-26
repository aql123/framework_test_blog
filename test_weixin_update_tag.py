import yaml
import requests
import pytest
import allure

@pytest.fixture(params=yaml.safe_load(open('test_get_tags.yaml','r',encoding='utf8')))
def test_get_tags(get_access_token1,request):
    get_url=request.param['url']+get_access_token1
    name = request.param['result']['name']
    res = requests.get(get_url)
    res_json=res.json()
    print(res_json)
    assert res.status_code == 200
    assert name == res_json['tags'][0]['name']
    return  res_json['tags'][-1]['id']


@pytest.mark.parametrize('updata',yaml.safe_load(open('test_updata_tag.yaml','r',encoding='utf8')))
def test_edit_tag(get_access_token1,test_get_tags,updata):
    url = updata['url']+get_access_token1
    data = updata['data']
    code = updata['result']['errcode']
    data['tag']['id'] = test_get_tags
    res=requests.post(url,json=data)
    assert res.status_code == 200
    print(res.json())
    assert res.json()['errcode'] == code

@pytest.mark.parametrize('delete',yaml.safe_load(open('test_delete_tag.yaml','r',encoding='utf8')))
def test_delete_tag(get_access_token1,delete,test_get_tags):
    url = delete['url']+get_access_token1
    json_data = delete['data']
    json_data['tag']['id'] = test_get_tags
    result = delete['result']
    res = requests.post(url,json=json_data)
    assert res.status_code == 200
    assert res.json() == result