import pytest

#无条件跳过
@pytest.mark.skip('待实现')
def test_sub():
    print("跳过啦，所以不会显示")

#根据条件跳过,这里我实际是先写了一个print(platform())来查看我的版本，读者可根据情况自行修改
#我也很好奇我明明win11怎么会打印win10，查阅发现10.0代表的就是win11，很奇怪的设计
from platform import platform
@pytest.mark.skipif(platform() == 'Windows-10-10.0.26100-SP0', reason='不支持该版本Windows')
def test_linux_cmd():
    print("跳过啦，所以不会显示")

#也可以使用@pytest.mark.xfail()来期望用例失败
@pytest.mark.xfail(reason='期望失败，3+4!=1')
def test_add():
    assert 3 + 4 == 3