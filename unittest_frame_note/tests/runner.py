import unittest

from .test_sumsub0 import SumSubTest0


def method_case():
    """添加单条或多条测试用例"""
    suite = unittest.TestSuite()

    case1 = SumSubTest0('test_sum01')
    case2 = SumSubTest0('test_sum02')
    case3 = SumSubTest0('test_sub01')

    suite.addTests([case1, case2, case3])

    runner = unittest.TextTestRunner()
    runner.run(suite)


def method_class():
    """添加一个测试用例类"""
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()
    # Return a suite of all test cases contained in testCaseClass
    suite.addTest(loader.loadTestsFromTestCase(SumSubTest0))

    runner = unittest.TextTestRunner()
    runner.run(suite)


def method_module():
    """添加一个或多个测试模块"""
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()

    # 相对路径导入时,start_dir必须也为相对路径
    start_dir = '..'
    suite.addTest(loader.discover(start_dir=start_dir, pattern="test_sumsub*.py"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
