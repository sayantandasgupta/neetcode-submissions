class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if len(stack) == 0 or stack[-1] != map_[ch]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0