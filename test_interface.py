import pytest
import requests
import yaml
test_input=[{"tag":{"name":"linda2112315"}},
            {"tag":{"name":"linda1256525"}}]



@pytest.mark.parametrize("test_input",test_input)
def test_eval(test_input):
#eval将字符串str当成有效的表达式来求值并返回计算结果
    print(test_input)
    #url=''
    #res=requests.post(url,json=test_input)
   # assert  res.status_code==200

#@pytest.fixture(params=[1,2,1,'linda'])
@pytest.fixture()
def login(request):
    return request.param

# @pytest.mark.parametrize('login',[1,2,3,'linda'])
# def test(login):
#     print(login)
@pytest.mark.parametrize('create',yaml.safe_load(open('test_data.yaml','r',encoding='utf8')))
def test_yaml(create):
     print(create['url'])
     print(create['data'])


