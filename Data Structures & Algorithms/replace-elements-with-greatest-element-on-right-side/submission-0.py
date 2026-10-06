class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = -1

        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]
            arr[i] = currMax

            if num >= currMax:
                currMax = num
            
        return arr
