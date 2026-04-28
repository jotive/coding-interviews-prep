import pytest

from problems.easy.p04_missing_number import find_missing_number


class TestFindMissingNumber:
    def test_middle_missing(self):
        assert find_missing_number([1, 2, 4, 5]) == 3

    def test_first_missing(self):
        assert find_missing_number([2, 3, 4, 5]) == 1

    def test_last_missing(self):
        assert find_missing_number([1, 2, 3, 4]) == 5

    def test_only_one_element(self):
        assert find_missing_number([1]) == 2

    def test_only_one_element_missing_first(self):
        assert find_missing_number([2]) == 1

    def test_empty_means_n_equals_1(self):
        assert find_missing_number([]) == 1

    def test_unsorted_input(self):
        assert find_missing_number([5, 3, 1, 2]) == 4

    @pytest.mark.parametrize(
        "nums,expected",
        [
            ([2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
            ([1, 3, 4, 5, 6, 7, 8, 9, 10], 2),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
            ([1, 2, 3, 4, 6, 7, 8, 9, 10], 5),
        ],
    )
    def test_n_equals_10(self, nums, expected):
        assert find_missing_number(nums) == expected

    def test_large_input(self):
        n = 10_000
        nums = [i for i in range(1, n + 1) if i != 7777]
        assert find_missing_number(nums) == 7777
