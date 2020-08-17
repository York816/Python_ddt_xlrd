from ddt import ddt, data, unpack
import unittest
from ReadExcelFile import readxls

datatest = readxls()


@ddt
class BiJiao(unittest.TestCase):
    @data(*datatest)  # 分离数据
    @unpack
    def test_sum(self, a, b):
        print('a取值={0},b取值={1},两者相加={2}'.format(int(a), float(b), int(a) + float(b)))


if __name__ == '__main__':
    unittest.main()
