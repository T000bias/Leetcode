import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        min_length = math.inf
        start_index = 0

        for index in range(0, len(nums)):
            window_sum += nums[index]
            while window_sum >= target:
                min_length = min(min_length, index - start_index + 1)
                window_sum -= nums[start_index]
                start_index += 1
        
        if min_length == math.inf:
            return 0

        return min_length