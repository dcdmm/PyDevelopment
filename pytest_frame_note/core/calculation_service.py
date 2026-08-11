class Recorder:
    def record(self, operation: str, result: int) -> bool:
        raise NotImplementedError


class CalculationService:
    def __init__(self, recorder: Recorder) -> None:
        self.recorder = recorder

    def add_and_record(self, left: int, right: int) -> int:
        result = left + right

        if not self.recorder.record("add", result):
            raise RuntimeError("计算结果记录失败!")

        return result
