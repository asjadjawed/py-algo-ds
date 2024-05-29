"""
Test for a simple BFS
"""

from py_algo_ds.algorithms.bfs import person_is_seller, search


def test_person_is_seller():
    assert person_is_seller("thom") is True
    assert person_is_seller("jonny") is False
    assert person_is_seller("alice") is False


def test_search():
    assert search("you") is True
    assert search("claire") is True
    assert search("alice") is False
    assert search("bob") is False
