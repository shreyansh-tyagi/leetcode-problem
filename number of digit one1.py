'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

 

Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 109
'''

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1: return 0
        p,c,result = 1,0,0 
        for char in str(n)[::-1]:
            d = int(char)
            if d == 1:
                result += c + n%(p) + 1
            elif d > 1:
                result += p + d*c
            c += p + (c<<3)+c 
            p = (p<<3)+p+p 
        return result