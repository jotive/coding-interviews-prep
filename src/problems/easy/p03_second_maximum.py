"""
Problem #3 — Second Maximum Element.

Find the second largest distinct value in a list without sorting.

Complexity:
    Time:  O(n) single pass.
    Space: O(1) two trackers.

Alternatives discarded:
    - sorted(set(nums))[-2]           -> O(n log n).
    - heapq.nlargest(2, set(nums))[-1] -> O(n log k); overkill for k=2.
    - max() twice + remove first       -> O(n) but mutates or copies input.

Contract:
    "Second maximum" means the second-largest *distinct* value.
    Returns None when no such value exists (empty list, all equal).
"""


def second_maximum(nums: list[int]) -> int | None:
    first = second = None
    for n in nums:
        if first is None or n > first:
            second = first
            first = n
        elif n != first and (second is None or n > second):
            second = n
    return second
