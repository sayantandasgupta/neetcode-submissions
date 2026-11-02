class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if stack[-1] != map_[ch]:
                    return False
                else:
                    stack.pop()

        return True