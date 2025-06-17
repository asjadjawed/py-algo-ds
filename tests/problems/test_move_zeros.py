import pytest
from py_algo_ds.problems.move_zeros import move_zeros


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 0, 2, 0, 0, 7], [1, 2, 7, 0, 0, 0]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 0], [1, 0]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([7, 11, 4], [7, 11, 4]),
        ([], []),
    ],
)
def test_move_zeros(nums: list[int], expected: list[int]):
    move_zeros(nums)
    assert nums == expected, f"Expected {expected}, but got {nums}"
