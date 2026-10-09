class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        stack = []
        for i in range(n):
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                temperature = stack.pop()
                result[temperature[1]] = i - temperature[1]
            
            stack.append((temperatures[i], i))

        return result
            
