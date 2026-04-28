import pytest

from problems.hard.p44_max_subarray import max_subarray_sum


class TestMaxSubarraySum:
    def test_classic_leetcode_case(self):
        assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_all_positive(self):
        assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

    def test_all_negative_returns_least_negative(self):
        assert max_subarray_sum([-5, -2, -8, -1, -3]) == -1

    def test_single_positive(self):
        assert max_subarray_sum([7]) == 7

    def test_single_negative(self):
        assert max_subarray_sum([-7]) == -7

    def test_single_zero(self):
        assert max_subarray_sum([0]) == 0

    def test_mixed_with_zero(self):
        assert max_subarray_sum([-1, 0, -1]) == 0

    def test_max_at_start(self):
        assert max_subarray_sum([10, -5, -5, -5]) == 10

    def test_max_at_end(self):
        assert max_subarray_sum([-5, -5, -5, 10]) == 10

    def test_max_spans_entire_array(self):
        assert max_subarray_sum([2, 3, -1, 4]) == 8

    def test_two_peaks_picks_larger(self):
        assert max_subarray_sum([3, -10, 5, 6]) == 11

    def test_two_peaks_picks_first_when_bigger(self):
        assert max_subarray_sum([5, 6, -10, 3]) == 11

    def test_raises_on_empty(self):
        with pytest.raises(ValueError):
            max_subarray_sum([])

    @pytest.mark.parametrize(
        "nums,expected",
        [
            ([1], 1),
            ([-1], -1),
            ([1, -1], 1),
            ([-1, 1], 1),
            ([1, 2, -1, 2], 4),
            ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
        ],
    )
    def test_parametrized(self, nums, expected):
        assert max_subarray_sum(nums) == expected

    def test_large_input_all_ones(self):
        assert max_subarray_sum([1] * 10_000) == 10_000

    def test_large_input_alternating(self):
        nums = [1 if i % 2 == 0 else -1 for i in range(10_000)]
        assert max_subarray_sum(nums) == 1
