

import requests
def get_token():
     get_url=' https://api.weixin.qq.com/cgi-bin/token'
     params={'grant_type':'client_credential',
        'appid':'wx1bbcb240d36a1d20',
        'secret':'d78121284a72d7bfdc76ad3ef9191703'
     }
     res=requests.get(get_url,params=params)
     res_json=res.json()
     return res_json['access_token']
def test_create_tag():
    url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token='+get_token()
    json_data={"tag":{"name":"linda999"}}
    res=requests.post(url,json=json_data)
    #res.json=res.json()
    print(res.json())
#test_create_tag()

#获取公众号已创建的标签
def test_get_tags():
    get_url='https://api.weixin.qq.com/cgi-bin/tags/get?access_token='+get_token()
    res=requests.get(get_url)
    res_json=res.json()
    print(res_json)
    print(res_json['tags'][-1])
    print(res_json['tags'][0]['name'])
    return res_json['tags'][-1]['id']

#test_get_tags()
def test_edit_tag():
    url='https://api.weixin.qq.com/cgi-bin/tags/update?access_token='+get_token()
    json_data={
        "tag":{"id":test_get_tags(),"name":"fanglida"
        }}
    res=requests.post(url,json=json_data)
    print(res.json())
test_edit_tag()