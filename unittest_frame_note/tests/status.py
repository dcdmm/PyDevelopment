import unittest


class StatusAnaly(unittest.TestCase):
    def test_1success(self):
        """通过(.)"""
        a = 3 + 4
        self.assertEqual(a, 7)

    def test_2fail(self):
        """失败(F)"""
        a = 3 + 4
        self.assertEqual(a, 9)

    def test_3exception(self):
        """异常(E)"""
        a = 3 + 4
        self.assertEqual(a, 7)
        raise Exception("异常")

    @unittest.skip("跳过")  # 跳过被此装饰器装饰的测试
    def test_4skip(self):
        """跳过(s)"""
        a = 3 + 4
        self.assertEqual(a, 7)


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(StatusAnaly))
runner = unittest.TextTestRunner()
runner.run(suite)
