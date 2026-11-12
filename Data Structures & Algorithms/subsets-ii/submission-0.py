class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(idx, nums, currSet, subsets):
            if idx >= len(nums):
                subsets.append(currSet.copy())
                return
            
            currSet.append(nums[idx])
            helper(idx + 1, nums, currSet, subsets)

            currSet.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            
            helper(idx + 1, nums, currSet, subsets)
        
        subsets, currSet = [], []
        nums.sort()
        helper(0, nums, currSet, subsets)

        return subsets