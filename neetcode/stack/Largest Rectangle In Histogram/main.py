class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        l = len(heights)
        rec_area = 0
        stack = []

        for x, h in enumerate(heights):
            start = x
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                rec_area = max(rec_area, height * (x - index))        
                start = index
            stack.append((start, h))

        for x, h in stack:
            rec_area = max(rec_area, h * (l - x))        

        return rec_area

sol = Solution()
heights = [7,1,7,2,2,4]
print(sol.largestRectangleArea(heights))