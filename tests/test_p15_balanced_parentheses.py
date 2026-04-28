import pytest

from problems.medium.p15_balanced_parentheses import is_balanced


class TestIsBalanced:
    @pytest.mark.parametrize(
        "s",
        [
            "",
            "()",
            "[]",
            "{}",
            "()[]{}",
            "([])",
            "{[()]}",
            "((()))",
            "[({})]",
            "a(b+c)*d",
            "func(arr[0], {key: val})",
        ],
    )
    def test_balanced(self, s):
        assert is_balanced(s) is True

    @pytest.mark.parametrize(
        "s",
        [
            "(",
            ")",
            "(]",
            "([)]",
            "(()",
            "())",
            "{[}]",
            "{",
            "}{",
            "[(])",
        ],
    )
    def test_unbalanced(self, s):
        assert is_balanced(s) is False

    def test_ignores_non_bracket_chars(self):
        assert is_balanced("hello world") is True
        assert is_balanced("123 + 456") is True

    def test_deeply_nested_balanced(self):
        assert is_balanced("(" * 500 + ")" * 500) is True

    def test_deeply_nested_unbalanced(self):
        assert is_balanced("(" * 500 + ")" * 499) is False
