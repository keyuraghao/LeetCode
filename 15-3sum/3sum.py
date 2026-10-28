class Solution(object):
    def threeSum(self, nums):
        target = 0
        ans = []
        nums.sort() #time = nlogn

        for idx,val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                threesum = nums[left] + val + nums[right]

                if threesum > target:
                    right -= 1
                elif threesum < target:
                    left += 1
                else:
                    ans.append([val,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return ans
        