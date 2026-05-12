class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # loop nums:
        # count
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]] + 1
            else:
                count[nums[i]] = 0
        max = len(nums) // 2
        for k, v in count.items():
            if v >= max:
                return k
