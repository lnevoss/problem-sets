class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        open = {'(', '{', '['}
        closed = {')', '}', ']'}
        stack = ['']

        for bracket in s:
            print(bracket)
            if bracket in open:
                stack.append(bracket)
            elif bracket in closed:
                if stack.pop() != closed[bracket]:
                    return False
            else:
                return False

        if len(stack) > 1:
            return False

        return True


sol = Solution()
s = "([{)}])"
s = '['
print(sol.isValid(s))
