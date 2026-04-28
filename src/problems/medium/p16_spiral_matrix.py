"""
Problem #16 — Spiral Matrix Traversal.

Given an m x n matrix, return all its elements in clockwise spiral order,
starting from the top-left corner.

Complexity:
    Time:  O(m * n)  — each cell visited exactly once.
    Space: O(1)      — excluding the output list; four integer boundaries only.

Alternatives discarded:
    - Direction vector + visited set   -> O(m*n) time but O(m*n) extra space
                                          for the visited grid. Also muddier
                                          control flow (must detect turns).
    - Recursive layer-by-layer peel    -> O(m*n) time, O(min(m,n)) stack
                                          depth. Same structure as the
                                          iterative boundary approach but
                                          harder to reason about edge cases
                                          (single row/column leftovers).
    - Rotate + pop first row repeatedly -> clever one-liner but O(m*n) extra
                                           space per rotation; not senior
                                           code, it's a party trick.

Boundary approach (top, bottom, left, right shrinking) is the senior-clean
choice: one loop, four straight-line traversals per layer, explicit guards
for the "row/column already consumed" case that bites naive implementations
on rectangular inputs.
"""


def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result: list[int] = []

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
