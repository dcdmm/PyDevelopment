def print_a_b(a, b):
    print(a + '\n' + b)


class Operate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        """加法操作"""
        result = self.a + self.b
        print(result)
        return result

    def subtraction(self):
        """减法操作"""
        result = self.a - self.b
        return result
