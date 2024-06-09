import sys
from io import StringIO

import pytest

from py_algo_ds.datastructures.binary_search_tree import (
    build_bst,
    in_order_traversal,
    post_order_traversal,
    pre_order_traversal,
)


def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = captured_stdout = StringIO()
    try:
        func(*args, **kwargs)
    finally:
        sys.stdout = old_stdout
    return captured_stdout.getvalue()


@pytest.mark.parametrize(
    "values, expected_in_order, expected_pre_order, expected_post_order",
    [
        (["x"], "", "", ""),
        (["5", "3", "x", "x", "8", "x", "x"], "3\n5\n8\n", "5\n3\n8\n", "3\n8\n5\n"),
        (["2", "1", "x", "x", "3", "x", "x"], "1\n2\n3\n", "2\n1\n3\n", "1\n3\n2\n"),
        (
            ["8", "5", "x", "7", "x", "x", "9", "x", "x"],
            "5\n7\n8\n9\n",
            "8\n5\n7\n9\n",
            "7\n5\n9\n8\n",
        ),
    ],
)
def test_binary_search_tree(
    values, expected_in_order, expected_pre_order, expected_post_order
):
    root = build_bst(values.copy())

    output = capture_output(in_order_traversal, root)
    assert output == expected_in_order

    output = capture_output(pre_order_traversal, root)
    assert output == expected_pre_order

    output = capture_output(post_order_traversal, root)
    assert output == expected_post_order
