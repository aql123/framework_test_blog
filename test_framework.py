import unittest
import requests


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s=requests.session()

    def setUp(self):
        url = "http://127.0.0.1:8000/admin/login/?next=/admin/"
        res=self.s.get(url)
        cookie=res.cookies
        dict_cookie = requests.utils.dict_from_cookiejar(cookie)
        self.csftoken = dict_cookie['csrftoken']
        assert 200 == res.status_code
        assert '用户名' in res.text
        assert 3 > res.elapsed.total_seconds()

    def test_post_login(self):
        url = "http://127.0.0.1:8000/admin/login/?next=/admin/"
        data = {
            'csrfmiddlewaretoken': self.csftoken,
            'username': 'linda',
            # 你的登录密码
            'password': '123456',
            'next': '/admin/',
        }
        res = self.s.post(url, data)
        print(res.text)
        assert 200 == res.status_code
        assert '分类' in res.text
        assert 3 > res.elapsed.total_seconds()

    def test_add_cate(self):
        pass
    def test_add_post(self):
        pass