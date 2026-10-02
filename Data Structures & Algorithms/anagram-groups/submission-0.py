class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)
        
        result = []

        for _, group in groups.items():
            result.append(group)

        return result