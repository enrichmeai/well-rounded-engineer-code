import pytest

from idioms.context_managers import Timer, temporary_setting


def test_timer_measures_the_block_with_a_fake_clock():
    ticks = iter([10.0, 12.5])
    with Timer(clock=lambda: next(ticks)) as timer:
        pass
    assert timer.elapsed == 2.5


def test_the_setting_is_restored_after_the_block():
    settings = {"debug": False}
    with temporary_setting(settings, "debug", True):
        assert settings["debug"] is True
    assert settings == {"debug": False}


def test_a_new_setting_is_removed_after_the_block():
    settings = {}
    with temporary_setting(settings, "colour", "blue"):
        assert settings["colour"] == "blue"
    assert settings == {}


def test_clean_up_runs_even_when_the_block_raises():
    settings = {"debug": False}
    with pytest.raises(RuntimeError):
        with temporary_setting(settings, "debug", True):
            raise RuntimeError("boom")
    assert settings == {"debug": False}
