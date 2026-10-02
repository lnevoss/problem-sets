class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        l, r = 0, n-1
        res = 0

        lm, rm = height[l], height[r]

        while l < r:

            if lm<rm:
                l+=1
                lm = max(lm, height[l])
                res += lm-height[l]
            else:
                r-=1
                rm = max(rm, height[r])
                res += rm-height[r]
                
        return res

sol = Solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]
height = [0,2,0,3,1,0,1,3,2,1]
print(sol.trap(height))