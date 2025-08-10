import pytest


@pytest.mark.xfail(reason="xfail test")
def test_with_bug():
    assert False


@pytest.mark.xfail(reason="xfail test исправлен")
def test_without_bug():
    pass
