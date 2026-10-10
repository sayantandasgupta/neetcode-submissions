class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p, s) for p, s in zip(position, speed)]
        
        arr.sort(key=lambda x : x[0], reverse=True)

        time_stack = []

        for pos, speed_ in arr:
            time = (target - pos) / speed_

            if len(time_stack) == 0:
                time_stack.append(time)
            elif time > time_stack[-1]:
                time_stack.append(time)

        return len(time_stack)