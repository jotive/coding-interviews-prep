import pytest

from problems.medium.p16_spiral_matrix import spiral_order


class TestSpiralOrder:
    def test_empty_matrix(self):
        assert spiral_order([]) == []

    def test_empty_inner(self):
        assert spiral_order([[]]) == []

    def test_single_element(self):
        assert spiral_order([[42]]) == [42]

    def test_single_row(self):
        assert spiral_order([[1, 2, 3, 4]]) == [1, 2, 3, 4]

    def test_single_column(self):
        assert spiral_order([[1], [2], [3], [4]]) == [1, 2, 3, 4]

    def test_square_3x3(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        assert spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def test_square_4x4(self):
        matrix = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7],
        ]
        assert spiral_order(matrix) == list(range(1, 17))

    def test_wide_rectangle_2x5(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [10, 9, 8, 7, 6],
        ]
        assert spiral_order(matrix) == list(range(1, 11))

    def test_tall_rectangle_5x2(self):
        matrix = [
            [1, 2],
            [8, 3],
            [7, 4],
            [6, 5],
            [10, 9],
        ]
        # Walk: 1,2 → 3,4,5 → (bottom row) 9,10 → (left column up) 6,7,8
        assert spiral_order(matrix) == [1, 2, 3, 4, 5, 9, 10, 6, 7, 8]

    def test_rectangle_3x4(self):
        matrix = [
            [1, 2, 3, 4],
            [10, 11, 12, 5],
            [9, 8, 7, 6],
        ]
        assert spiral_order(matrix) == list(range(1, 13))

    def test_rectangle_4x3(self):
        matrix = [
            [1, 2, 3],
            [10, 11, 4],
            [9, 12, 5],
            [8, 7, 6],
        ]
        assert spiral_order(matrix) == list(range(1, 13))

    @pytest.mark.parametrize(
        "matrix,expected",
        [
            ([[1, 2], [4, 3]], [1, 2, 3, 4]),
            ([[1]], [1]),
            ([[1, 2, 3]], [1, 2, 3]),
            ([[1], [2], [3]], [1, 2, 3]),
        ],
    )
    def test_small_cases(self, matrix, expected):
        assert spiral_order(matrix) == expected

    def test_preserves_original(self):
        matrix = [[1, 2], [3, 4]]
        snapshot = [row[:] for row in matrix]
        spiral_order(matrix)
        assert matrix == snapshot

    def test_negatives_and_zeros(self):
        matrix = [
            [-1, 0, 1],
            [-2, 0, 2],
            [-3, 0, 3],
        ]
        assert spiral_order(matrix) == [-1, 0, 1, 2, 3, 0, -3, -2, 0]
