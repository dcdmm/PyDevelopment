import unittest

from ..core.calculator import MyMath


class SumSubTest0(unittest.TestCase):  # 测试类需要继承unittest.TestCase

    def setUp(self):
        """测试方法;每个测试方法执行前先运行setUp()"""
        print("开始执行测试用例{}...".format(self))

    # 测试方法名称必须以test开头
    # 根据ASCII顺序依次执行:test_sub01、test_sub02、test_sum01、test_sum_02
    def test_sum01(self):
        m = MyMath(3, 4)
        print(m)
        self.assertEqual(m.sum(), 7) # unittest框架断言

    def test_sum02(self):
        m = MyMath(2, 8)
        print(m)
        self.assertEqual(m.sum(), 12)

    def test_sub01(self):
        m = MyMath(3, 4)
        print(m)
        self.assertEqual(m.sub(), -1)

    def test_sub02(self):
        m = MyMath(5, 1)
        print(m)
        self.assertEqual(m.sub(), 343)

    def tearDown(self):
        """测试方法;每个测试方法执行完毕后都要执行tearDown()方法"""
        print("测试用例{}执行结束...".format(self))
