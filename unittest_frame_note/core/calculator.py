class Calculator:
    def __init__(self, left: int | str, right: int | str) -> None:
        try:
            self.left = int(left)
            self.right = int(right)
        except (TypeError, ValueError) as error:
            raise ValueError("operands must be integers") from error

    def add(self) -> int:
        return self.left + self.right

    def subtract(self) -> int:
        return self.left - self.right

    def divide(self) -> float:
        if self.right == 0:
            raise ZeroDivisionError("right operand cannot be zero")
        return self.left / self.right
