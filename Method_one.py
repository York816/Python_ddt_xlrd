"""
DDT简介
Data Driven Testing，数据驱动，简单来说就是测试数据的参数化

Python数据驱动模块DDT，包含类的装饰器ddt和两个方法装饰器data（直接输入测试数据）

通常情况下，data中的数据按照一个参数传递给测试用例，如果data中含有多个数据，以元组，列表，字典等数据，需要自行在脚本中对数据进行分解或者使用unpack分解数据。

@data(*参数)

拆分参数为多个，运行多次用例

@data(a,b)

那么a和b各运行一次用例

@data([a,d],[c,d])

如果没有@unpack，那么[a,b]当成一个参数传入用例运行

如果有@unpack，那么[a,b]被分解开，按照用例中的两个参数传递
"""


from ddt import ddt, data, unpack
import unittest
from ReadExcelFile import readxls

datatest = readxls()


@ddt
class BiJiao(unittest.TestCase):

    @data(*datatest)  # 分离数据
    def test_sum(self, data):
        a, b = data  # 将列表的值赋值给a，b
        print('a取值={0},b取值={1},两者相加={2}'.format(int(a), float(b), int(a) + float(b)))


if __name__ == '__main__':
    unittest.main()
