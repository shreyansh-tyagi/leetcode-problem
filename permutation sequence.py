'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!

'''
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a=''
        for i in range(1,n+1):
            a+=str(i)
        b=list(permutations(a))
        c=b[k-1]
        d=''
        for i in range(len(c)):
            d+=c[i]
        return d    