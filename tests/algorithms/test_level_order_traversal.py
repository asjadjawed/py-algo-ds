"""
Tests for Level Order Traversal
"""

from py_algo_ds.algorithms.level_order_traversal import Node, level_order_traversal


def test_level_order_traversal():
    # Test case 1: Typical case
    root = Node(1, Node(2), Node(3, Node(4), Node(5)))
    assert level_order_traversal(root) == [[1], [2, 3], [4, 5]]

    # Test case 2: Single node
    root = Node(1)
    assert level_order_traversal(root) == [[1]]

    # Test case 3: Empty tree
    assert level_order_traversal(None) == []

    # Test case 4: Larger tree out of order tree
    root = Node(1, Node(2, Node(5), Node(4)), Node(3, Node(6), Node(7)))
    assert level_order_traversal(root) == [[1], [2, 3], [5, 4, 6, 7]]
