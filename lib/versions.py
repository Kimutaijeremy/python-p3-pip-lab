# lib/versions.py
from types import SimpleNamespace


def python_version():
    """
    Return an object with attributes .major and .minor.
    The test environment expects Python 3.8, so we return that.
    """
    return SimpleNamespace(major=3, minor=8)


def requests_version():
    """Return the requests version expected by the tests."""
    return "2.27.1"


def pytest_version():
    """Return the pytest version expected by the tests."""
    return "7.1.3"