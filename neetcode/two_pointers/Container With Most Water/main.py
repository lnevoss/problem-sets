class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        l, r = 0, n-1
        maxArea = 0
        
        while l < r:
            currArea = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, currArea)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea

sol = Solution()
height = [1,7,2,5,4,7,3,6]
print(sol.maxArea(height))