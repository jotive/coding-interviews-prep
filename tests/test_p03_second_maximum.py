import pytest

from problems.easy.p03_second_maximum import second_maximum


class TestSecondMaximum:
    def test_typical_case(self):
        assert second_maximum([3, 1, 4, 1, 5, 9, 2, 6]) == 6

    def test_sorted_ascending(self):
        assert second_maximum([1, 2, 3, 4, 5]) == 4

    def test_sorted_descending(self):
        assert second_maximum([5, 4, 3, 2, 1]) == 4

    def test_with_duplicates_of_max(self):
        assert second_maximum([5, 5, 3, 2]) == 3

    def test_negative_numbers(self):
        assert second_maximum([-10, -20, -30]) == -20

    def test_mixed_signs(self):
        assert second_maximum([-1, 0, 1]) == 0

    def test_two_distinct_elements(self):
        assert second_maximum([1, 2]) == 1

    def test_two_equal_elements(self):
        assert second_maximum([5, 5]) is None

    def test_all_equal(self):
        assert second_maximum([7, 7, 7, 7]) is None

    def test_single_element(self):
        assert second_maximum([42]) is None

    def test_empty(self):
        assert second_maximum([]) is None

    def test_max_at_end(self):
        assert second_maximum([3, 1, 4, 1, 5]) == 4

    def test_max_at_start(self):
        assert second_maximum([100, 3, 2, 1]) == 3

    def test_many_duplicates_then_new_max(self):
        assert second_maximum([2, 2, 2, 2, 5]) == 2

    @pytest.mark.parametrize(
        "nums,expected",
        [
            ([1, 1, 2], 1),
            ([2, 1, 1], 1),
            ([1, 2, 1], 1),
        ],
    )
    def test_duplicate_min_positions(self, nums, expected):
        assert second_maximum(nums) == expected
