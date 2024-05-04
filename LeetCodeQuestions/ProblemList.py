from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for key, item in enumerate(nums):
            second_nums = nums[key+1:]
            for item1 in second_nums:
                if item + item1 == target:
                    return ([key, nums.index(item1, key+1)])

        return -1

