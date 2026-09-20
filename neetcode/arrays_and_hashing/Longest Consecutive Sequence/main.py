class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        longest = 0

        for num in nums: 
            #look for possible start of sequence
            if (num - 1) not in nums:
                length = 1
                #look for continuation of given sequence
                while (num + length) in nums:
                   length += 1 
                longest = max(length, longest)

        return longest
    
# sol = Solution()
# nums=[9,1,4,7,3,-1,0,5,8,-1,6]
# nums=[0,0]
# nums=[1, 2, 3, 100, 4, 200]
# nums=[1000000000,999999999,-1000000000,-999999999,-999999998,5]
# print(sol.longestConsecutive(nums))