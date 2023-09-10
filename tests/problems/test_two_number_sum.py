"""
Test for two number sum
"""

from py_algo_ds.problems.two_number_sum import two_number_sum


class TestTwoNumberSum():
    """Test two sum problem"""

    def test_valid_pair(self):
        """valid pair test"""
        result = two_number_sum([2, 7, 11, 15], 9)
        assert result is not None and sorted(result) == sorted([2, 7])

    def test_negative_numbers(self):
        """with negative numbers"""
        result = two_number_sum([-1, 2, 3, 4], 3)
        assert result is not None and sorted(result) == sorted([-1, 4])

    def test_no_solution(self):
        """no solution"""
        assert two_number_sum([1, 2, 3, 4], 10) is None

    def test_large_numbers(self):
        """large numbers"""
        result = two_number_sum([1000000, 2000000, 3000000], 5000000)
        assert result is not None and sorted(
            result) == sorted([2000000, 3000000])

    def test_empty_list(self):
        """empty list"""
        assert two_number_sum([], 7) is None

    def test_list_of_two_elements(self):
        """only two elements"""
        result = two_number_sum([3, 4], 7)
        assert result is not None and sorted(result) == sorted([3, 4])

    def test_list_of_one_element(self):
        """single element"""
        assert two_number_sum([7], 7) is None
