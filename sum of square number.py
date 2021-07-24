'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true
 

Constraints:

0 <= c <= 231 - 1

'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n=int(math.sqrt(c))
        i,j=0,n
        while i<=j:
            res=i*i+j*j
            if res==c:
                return True
            elif res>c:
                j-=1
            else:
                i+=1
        return False