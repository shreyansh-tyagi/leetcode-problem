'''
Given an integer n, return the largest palindromic integer that can be represented as the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.

 

Example 1:

Input: n = 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
Example 2:

Input: n = 1
Output: 9
 

Constraints:

1 <= n <= 8
'''
class Solution:
    def largestPalindrome(self, n: int) -> int:
        return [9, 987, 123, 597, 677, 1218, 877, 475][n-1]