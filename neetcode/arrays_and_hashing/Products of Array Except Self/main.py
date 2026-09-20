class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        #prefix array of every product before index
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        #suffix array of every product after index
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        #products of prefix and suffix arrays at any given index
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res