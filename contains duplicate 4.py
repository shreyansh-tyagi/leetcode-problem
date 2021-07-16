'''
Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
 

Constraints:

0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1

'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums)==len(list(set(nums))) and t==0:
            return False
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if i==j:
                    continue
                elif abs(nums[i]-nums[j])<=t and abs(i-j)<=k:
                    return True
        return False        
    