class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = [0] * 26
        ord_a = ord('a')

        for char_s, char_t in zip(s,t):
            chars[ord(char_s) - ord_a] += 1
            chars[ord(char_t) - ord_a] -= 1

        return not any(chars)