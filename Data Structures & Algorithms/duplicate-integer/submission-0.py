class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for _, value in freq.items():
            if value > 1:
                return True

        return False