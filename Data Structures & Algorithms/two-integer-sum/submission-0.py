class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}

        for i in range(len(nums)):
            if target - nums[i] in map_:
                return [map_[target - nums[i]], i]
            
            map_[nums[i]] = i

        return [-1, -1]