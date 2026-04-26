class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and asteroids[i] < 0 < stack[-1]:
                diff = asteroids[i] + stack[-1]
                if diff < 0:
                    stack.pop()
                    continue
                elif diff == 0:
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        return stack