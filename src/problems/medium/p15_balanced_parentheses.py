"""
Problem #15 — Balanced Parentheses.

Given a string containing brackets `()`, `[]`, `{}` (possibly with other chars
interleaved), determine whether every opening bracket has a matching closer in
the correct order.

Complexity:
    Time:  O(n) single pass.
    Space: O(n) worst case (all openers).

Alternatives discarded:
    - Regex-based collapse  -> elegant but O(n^2) in the worst case due to
                               repeated scans; bad for long inputs.
    - Counter per bracket    -> fails on "([)]"; order matters, counts don't.

Stack is the canonical tool: each opener pushes, each closer must match the
top. Mismatch or empty stack on closer = not balanced. Non-bracket chars are
ignored (the problem statement leaves this underspecified; we take the more
lenient interpretation so the solution works for "(a+b)*c" style inputs).
"""

_PAIRS = {")": "(", "]": "[", "}": "{"}
_OPENERS = frozenset(_PAIRS.values())
_CLOSERS = frozenset(_PAIRS.keys())


def is_balanced(s: str) -> bool:
    stack: list[str] = []
    for ch in s:
        if ch in _OPENERS:
            stack.append(ch)
        elif ch in _CLOSERS:
            if not stack or stack.pop() != _PAIRS[ch]:
                return False
    return not stack
