'''
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

'''
class Solution(object):

    def countPrimes(self, n):
        if n<=2:
            return 0
        a=[2]
        for i in range(3, n):
            j=0
            for j in a:
                if i%j ==0:                    
                    break
                if j**2>i:
                    a.append(i)
                    break    
        return len(a)