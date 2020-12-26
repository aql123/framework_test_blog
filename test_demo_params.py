import pytest
@pytest.mark.parametrize('num1,num2,result',[[1,2,3],[2,3,5],[1.2,3.4,4.5]])


def test_calctor(num1,num2,result):
    print(num1)
    print(num2)
    print(result)
    assert num1+num2==result
