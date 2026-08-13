from unittest.mock import Mock
import pytest

from core import CalculationService
from core import monkeypatch_demo


def test_01() -> None:
    recorder = Mock()  # 模拟真实对象

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

    # (断言)检查recorder.record(...)只被调用一次且参数为"add", 13
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


def test_03(monkeypatch: pytest.MonkeyPatch) -> None: 
    # 调用fake_get_data()时返回"fake data"
    fake_get_data = Mock(return_value="fake data")

    # **暂时**把monkeypatch_demo.get_data替换为fake_get_data
    monkeypatch.setattr(monkeypatch_demo, "get_data", fake_get_data)

    result = monkeypatch_demo.process_data()

    assert result == "processed: fake data"

    fake_get_data.assert_called_once_with()

    # test_03测试结束后,monkeypatch_demo.get_data被恢复


def test_04_monkeypatch_has_restored_real_function() -> None:
    # 此时process_data()内部调用是monkeypatch_demo.get_data
    result = monkeypatch_demo.process_data()

    assert result == "processed: real data"
