import pytest
@pytest.fixture(scope='function')
def open():
    print("打开浏览器")
    yield
    print("关闭浏览器")

@pytest.mark.usefixtures("open")
def test_so():
    print("输入关键字")

@pytest.mark.usefixtures("open")
def test_baike():
    print("baike")