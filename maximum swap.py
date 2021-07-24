'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
Accepted
105,812
Submissions
231,831

'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        n,b=str(num),[]
        for i in n:
            b.append(int(i))
        c,d=max(b),b.index(max(b))
        b[d],b[0],e=b[0],c,'' 
        for i in b:
            e+=str(i)
        return int(e)
        