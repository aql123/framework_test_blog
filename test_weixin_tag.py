import requests
import pytest
import yaml

# 通过yaml创建标签
# 打开读取yaml文件
@pytest.mark.parametrize('create',yaml.safe_load(open('test_data.yaml','r',encoding='utf8')))
def test_create_tag(get_access_token1,create):
    url = create['url'] + get_access_token1
    json_data = create['data']
    result = create['result']['name']       # result中内容 预期结果
    res = requests.post(url, json=json_data)
    assert 200 == res.status_code
    assert res.json()['tag']['name'] == result
    # print(res.json())