import pytest
from py_algo_ds.problems.remove_duplicates import remove_duplicates


@pytest.mark.parametrize(
    "nums, expected_length, expected_nums",
    [
        ([0, 0, 1, 1, 1, 2, 2], 3, [0, 1, 2]),
        ([1, 1, 2], 2, [1, 2]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 1, 1, 1], 1, [1]),
        ([], 0, []),
        ([3], 1, [3]),
        ([4, 4], 1, [4]),
        ([4, 5], 2, [4, 5]),
        ([0, 0, 0, 0, 0, 1], 2, [0, 1]),
        ([0, 0, 1, 1, 1, 2, 2, 200, 200, 300, 3000], 6, [0, 1, 2, 200, 300, 3000]),
    ],
)
def test_remove_duplicates(nums, expected_length, expected_nums):
    length = remove_duplicates(nums)
    assert length == expected_length
    assert nums[:length] == expected_nums
