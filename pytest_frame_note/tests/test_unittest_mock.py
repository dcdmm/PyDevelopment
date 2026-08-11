from unittest.mock import Mock
import pytest

from core import CalculationService



def test_01() -> None:
    recorder = Mock()  # 模拟真实的Recorder对象

    # 规定调用recorder.record(...)时返回True
    recorder.record.return_value = True 

    # 与上等价
    # recorder = Mock()
    # recorder.record = Mock(return_value=True)

    # 与上等价
    # recorder = Mock(record=Mock(return_value=True))

    service = CalculationService(recorder)
    result = service.add_and_record(10, 3)

    assert result == 13

    # (断言)确认recorder.record(...)只被调用一次且参数为"add", 13
    recorder.record.assert_called_once_with("add", 13)


def test_02() -> None:
    recorder = Mock()

    # 规定调用recorder.record(...)时返回False
    recorder.record.return_value = False
    service = CalculationService(recorder)

    # match会检查异常消息中是否包含"计算结果记录失败"
    with pytest.raises(RuntimeError, match="计算结果记录失败"):
        service.add_and_record(10, 3)

    recorder.record.assert_called_once_with("add", 13)  # 同样进行了一次调用