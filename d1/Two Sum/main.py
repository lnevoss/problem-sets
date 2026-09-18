class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []

        for x in range(len(nums)):
            op1 = nums[x]
            seen.append(op1)
            for y in range(0, x):
                op2 = seen[y] 
                if op1 + op2 == target:
                    return [seen.index(op2), len(seen)-1]

        return