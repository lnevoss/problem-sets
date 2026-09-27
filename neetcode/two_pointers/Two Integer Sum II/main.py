class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if not numbers:
            return []
        
        l, r = 0, len(numbers) - 1

        while l < r:
            if (numbers[l] + numbers[r] > target):
                r -= 1
            elif (numbers[l] + numbers[r] == target):
                return [l+1,r+1]
            else:
                l += 1
        
        return []

sol = Solution()
numbers=[-1,0]
target = -1
numbers=[-5,-3,0,2,4,6,8]
target=5
print(sol.twoSum(numbers, target))