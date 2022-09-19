"""
Testing Module for main
"""

from py_algo_ds.main import hello


def test_hello():
    """test hello function
    """
    assert hello() == "Hello Python!"
