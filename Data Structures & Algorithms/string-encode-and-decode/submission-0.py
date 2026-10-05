class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "".join([f"{len(s)}#{s}" for s in strs])
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        idx = 0

        while idx < len(s):
            length = []
            while s[idx].isalnum() and s[idx] != "#":
                length.append(s[idx])
                idx += 1
            length = int("".join(length))
            idx += 1
            str_len = 0
            temp = []
            while idx < len(s) and str_len < length:
                temp.append(s[idx])
                idx += 1
                str_len += 1
            decoded_strs.append("".join(temp))
        
        return decoded_strs