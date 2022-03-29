import unittest

from ..core.calculator import MyMath


class SumSubTest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """A class method called before tests in an individual class are run"""
        print("开始执行测试用例{}...".format(cls))

    def test_sum01(self):
        m = MyMath(3, 4)
        print(m)
        self.assertEqual(m.sum(), 7)

    def test_sum02(self):
        m = MyMath(2, 8)
        print(m)
        self.assertEqual(m.sum(), 11)

    def test_sub01(self):
        m = MyMath(3, 4)
        print(m)
        self.assertEqual(m.sub(), -1)

    def test_sub02(self):
        m = MyMath(5, 1)
        print(m)
        self.assertEqual(m.sub(), 343)

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        print("测试用例{}执行结束...".format(cls))
