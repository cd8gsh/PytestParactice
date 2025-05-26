import pytest

@pytest.mark.parametrize('name, age', [('小明', 18), ('王林', 16)], ids=["第一个人","第二个人"])
def test_example_3(name, age):
    print(f'测试参数: {name}, {age}')