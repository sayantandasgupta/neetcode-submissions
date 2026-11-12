class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, i, subsets, curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            helper(nums, i+1, subsets, curSet)

            curSet.pop()
            helper(nums, i + 1, subsets, curSet)
        
        subsets, curSet = [], []
        helper(nums, 0, subsets, curSet)

        return subsets