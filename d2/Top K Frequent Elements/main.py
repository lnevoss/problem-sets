class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = {}

        for x in nums:
            if x not in res:
                res[x] = 0
            res[x]+=1
        
        return list({k: v for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True)[:k]}.keys())
    

nums = [1,2,2,3,3,3,3,3,1,2,4]
k = 4
sol = Solution()

print(sol.topKFrequent(nums,k))