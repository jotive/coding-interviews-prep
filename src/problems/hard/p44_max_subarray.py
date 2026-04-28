"""
Problem #44 — Maximum Subarray Sum (Kadane's algorithm).

Given a list of integers, return the largest possible sum of a contiguous
(non-empty) subarray.

Complexity:
    Time:  O(n) single pass.
    Space: O(1).

Alternatives discarded:
    - Brute force: try every (i, j) pair -> O(n^2) or O(n^3).
    - Divide & conquer: split, recurse, merge with "max crossing" -> O(n log n).
      Elegant, interviewable, but Kadane dominates in practice and is easier to
      extend (indices, circular variant, 2D).
    - Prefix sums + min-so-far: O(n) / O(n). Correct, but Kadane is strictly
      smaller in space and reads more directly as "running choice".

The core insight is a single DP recurrence:

    best_ending_here(i) = max(nums[i], best_ending_here(i-1) + nums[i])

Read: "at each position, either start fresh or extend the previous run."
The global answer is the max of best_ending_here across all i.

Edge case: all-negative arrays. The contract here says "non-empty contiguous
subarray", so we return the least-negative single element. Returning 0 for
all-negative inputs is a *different* problem ("non-empty OR empty subarray")
and would silently hide bugs in callers that care about the actual max.

Contract:
    `nums` is non-empty. Empty input raises ValueError — the notion of "max
    subarray sum" is undefined without at least one element, and silently
    returning 0 has bitten real systems.
"""


def max_subarray_sum(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")

    best_ending_here = best_overall = nums[0]
    for n in nums[1:]:
        best_ending_here = max(n, best_ending_here + n)
        best_overall = max(best_overall, best_ending_here)
    return best_overall
