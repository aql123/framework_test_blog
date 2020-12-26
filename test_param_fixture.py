import pytest

test_user_data=["linda","servenruby"]
@pytest.fixture(scope="module")
def login(request):
    #这个方法是接受传入的参数，接受一个参数

    user=request.param
    print("\n打开首页准备登陆，登陆用户：%s" % user)
    return user
#这是pytest的参数化，数据驱动，indeirect=True,是把login_r当做函数去执行
@pytest.mark.parametrize("login",test_user_data,indirect=True)
def test_login(login ):

    #登陆用例
    a=login
    print("测试用例中login的返回值：%s" % a)
    assert a !=""