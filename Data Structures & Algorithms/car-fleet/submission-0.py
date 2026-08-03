class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        car = sorted(zip(position, speed), reverse=True)
        for (p, s) in car:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)



        