'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000

'''
import numpy
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse =True)
        a = nums[0]*nums[1]*nums[2]
        b = nums[-1]*nums[-2]*nums[0]
        return max([a,b])