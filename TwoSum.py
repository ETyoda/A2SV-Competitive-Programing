class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Hash map to store values and their indices

        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                # If the complement is found in the map, return the indices
                return [num_map[complement], i]
            else:
                # Add the current number and its index to the map
                num_map[num] = i

        # No valid solution found
        return []

