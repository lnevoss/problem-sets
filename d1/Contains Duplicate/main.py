class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = False
        size = len(nums)

        seen = set()
        duplicate_set = set()

        for num in nums:
            if num in seen:
                duplicate_set.add(num)
            else:
                seen.add(num)

        if len(duplicate_set) > 0:
            hasDuplicate = True
                    
        return hasDuplicate