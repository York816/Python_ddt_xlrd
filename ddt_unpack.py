from ddt import ddt, data, unpack
import unittest


@ddt
class Test(unittest.TestCase):
    name = [['橙子', '橘子'], ['柠檬', '柚子'], ['苹果', '桃子'], ['桃子', '杨桃']]

    @data(*name)
    @unpack
    def test(self, name1, name2):
        print(name1, name2)


if __name__ == '__main__':
    unittest.main()
