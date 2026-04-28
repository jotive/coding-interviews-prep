"""
Problem #4 — Find Missing Number.

Array of n-1 distinct integers from the range [1, n]. Find the missing one.

Complexity:
    Time:  O(n) single pass.
    Space: O(1) accumulator.

Alternatives discarded:
    - set(range(1, n+1)) - set(nums)  -> O(n) time but O(n) space.
    - sort and scan                    -> O(n log n) time.
    - XOR trick (a ^ i for i in 1..n)  -> O(n) / O(1) but arithmetic is clearer
                                          and avoids confusion during review.

The Gauss formula is the textbook move: n*(n+1)/2 - sum(nums).

Contract:
    `nums` has length n-1 and contains distinct integers in [1, n].
    Returns the one missing integer.
    Inputs outside that contract are the caller's problem.
"""


def find_missing_number(nums: list[int]) -> int:
    n = len(nums) + 1
    expected = n * (n + 1) // 2
    return expected - sum(nums)
