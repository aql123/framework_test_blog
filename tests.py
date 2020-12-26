from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.

# 在协议层和接口层发送请求的第三方库
import requests

class TestBlogLogin():
    # 初始化，使用session保存状态的方式提交请求
    def __init__(self):
        self.s = requests.session()
    # 打开登录页
    def get_login(self):
        url = "http://127.0.0.1:8000/admin/login/?next=/admin/"
        res = self.s.get(url)
        assert 200 == res.status_code
        # print(res.text)
        assert '用户名'in res.text
        assert 3>res.elapsed.total_seconds()
        # 返回的cookies，是个jar的对象
        cookie = res.cookies
        # print(cookie)
        # 使用工具，jar对象转成dict
        dict_cookie = requests.utils.dict_from_cookiejar(cookie)
        # print(dict_cookie)
        self.csftoken=dict_cookie['csrftoken']
    #输入用户名和密码提交
    def post_login(self):
        url="http://127.0.0.1:8000/admin/login/?next=/admin/"
        data={
            'csrfmiddlewaretoken':self.csftoken,
            'username':'linda',
            #你的登录密码
            'password':'123456',
            'next':'/admin/',
        }
        res=self.s.post(url,data)
        print(res.text)
        assert'分类'in res.text
        #打开分类添加页
    def get_add_category(self):
        url='http://127.0.0.1:8000/admin/blog/category/add/'
        res = self.s.get(url)
        cookie = res.cookies
        dict_cookie = requests.utils.dict_from_cookiejar(cookie)
        self.csftoken_add_cate = dict_cookie['csrftoken']
        print(self.csftoken_add_cate)

    def post_add_category(self):
        url = 'http://127.0.0.1:8000/admin/blog/category/add/'
        data={
            'csrfmiddlewaretoken': self.csftoken_add_cate,
            'name':'docker1',
            'save':'保存',
        }
        res=self.s.post(url,data)
        assert 'docker1' in res.text




login=TestBlogLogin()
login.get_login()
login.post_login()
login.get_add_category()







