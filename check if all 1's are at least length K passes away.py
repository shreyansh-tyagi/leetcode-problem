'''
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

 

Example 1:



Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:



Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true
Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true
 

Constraints:

1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1

'''
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        a,b=0,[]
        for i in nums:
            if i ==1:
                b.append(a)
                a=0
            else:
                a+=1
        if 0 in b:   
            b.remove(0)
        c=0
        for i in b:
            if i>=k:
                c+=1
        if c==len(b):
            return True
        else:
            return False