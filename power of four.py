'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        a,b=0,0
        if n==0:
            return False
        while(a!=n and a<n):
            a=4**b
            b+=1
        if a==n:
            return True
        else:
            return False