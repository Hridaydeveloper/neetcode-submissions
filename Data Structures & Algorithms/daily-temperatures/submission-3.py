class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        i = len(temperatures) - 1

        while i >= 0:
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if len(stack) == 0:
                greater = 0
            else:
                greater = stack[-1] - i

            result[i] = greater
            stack.append(i)

            i -= 1
        return result

