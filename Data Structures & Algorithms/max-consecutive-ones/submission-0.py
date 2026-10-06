class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        sum_ = 0

        for num in nums:
            if num == 1:
                sum_ += 1
            else:
                max_count = max(max_count, sum_)
                sum_ = 0

        max_count = max(max_count, sum_)

        return max_count