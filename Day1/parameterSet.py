import pytest

#单个参数，多种用例测试
@pytest.mark.parametrize('args', ['张三', '李四', '王五'])
def test_example_1(args):
    print(f'测试参数: {args}')

#多个参数，多种用例测试
#第一个参数为字符串格式，用于描述传入的多种参数的名称，用逗号隔开，实际使用中允许,后有空格
#第二个参数 为列表格式，每组测试用例用元组形式传递
@pytest.mark.parametrize('name, age', [('小明', 18), ('王林', 16)])
def test_example_2(name, age):
    print(f'测试参数: {name}, {age}')

#还可以为每组测试用例添加自定义说明(id)
@pytest.mark.parametrize('name, age', [('小明', 18), ('王林', 16)], ids=["第一个人","第二个人"])
def test_example_3(name, age):
    print(f'测试参数: {name}, {age}')

"""这里期望用调用函数的方法输出，
实际从 print("开始测试2")没有输出可以看出，
在使用装饰器@pytest.mark.parametrize后，
函数已经自动被pytest调用"""

print(__name__)
if __name__ == '__main__':
    test_example_1()
    print("开始测试2")
    test_example_2()

"""实践证明19~23行代码不影响输出结果，
可以自己注释以后查看
由于go to 到源码没能很看懂实现方式，
但通过print(__name__)没有输出
以及运行输出形式为Test Results
估计是 直接调用了pytest作为解释器来运行上述程序，对于非test开头的类、函数方法直接跳过"""