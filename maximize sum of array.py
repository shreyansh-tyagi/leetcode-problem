'''
Given an array nums of integers, we must modify the array in the following way: we choose an i and replace nums[i] with -nums[i], and we repeat this process k times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose indices (1,) and nums becomes [4,-2,3].
Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
 

Note:

1 <= nums.length <= 10000
1 <= k <= 10000
-100 <= nums[i] <= 100

'''
class Solution:
    def largestSumAfterKNegations(self, nums:List[int],k: int)->int:
        a,i=sorted(nums),0
        while k>0:
            if a[i] <= a[i+1]:
                a[i] = a[i]*-1
                k-=1
            else:
                i += 1
        return sum(a)
