class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
            kk=target-nums[i]
            if kk in nums[i+1:]:
                    return [i,nums[i+1:].index(kk)+i+1]

