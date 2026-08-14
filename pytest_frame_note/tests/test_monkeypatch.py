from pathlib import Path
from unittest.mock import Mock
import pytest

from core import monkeypatch_demo


def test_01(monkeypatch: pytest.MonkeyPatch) -> None: 
    # 调用fake_get_data()时返回"fake data"
    fake_get_data = Mock(return_value="fake data")

    # **暂时**把monkeypatch_demo.get_data替换为fake_get_data
    monkeypatch.setattr(monkeypatch_demo, "get_data", fake_get_data)

    result = monkeypatch_demo.process_data()

    assert result == "processed: fake data"

    fake_get_data.assert_called_once_with()

    # test_01测试结束后,恢复为monkeypatch_demo.get_data


def test_02() -> None:
    # 此时process_data()内部调用是monkeypatch_demo.get_data
    result = monkeypatch_demo.process_data()

    assert result == "processed: real data"


def test_03(
    monkeypatch: pytest.MonkeyPatch, 
    tmp_path: Path
) -> None:
    work_dir = tmp_path / "project"
    work_dir.mkdir()
    (work_dir / "config.txt").write_text("mode=test", encoding="utf-8")

    # **暂时**把当前工作目录切换到work_dir
    monkeypatch.chdir(work_dir)

    assert Path.cwd() == work_dir
    assert Path("config.txt").read_text(encoding="utf-8") == "mode=test"