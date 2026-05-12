class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # loop nums:
        # count
        count = {}
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            if i in count:
                count[i] += 1
                if count[i] > len(nums)/2:
                    return i
            else:
                count[i] = 1
