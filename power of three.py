'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
Example 4:

Input: n = 45
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        a,b=0,0
        if n==0:
            return False
        while(a!=n and a<n):
            a=3**b
            b+=1
        if a==n:
            return True
        else:
            return False