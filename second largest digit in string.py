'''
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.

'''
class Solution:
    def secondHighest(self, s: str) -> int:
        c='abcdefghijklmnopqrstuvwxyz'
        a=sorted(s)
        b=0
        for i in range(len(a)):
            if a[i]==a[i+1]:
                pass
            else:
                b=a[i+1]
                break
        if b not in c:
            return (int(b))
        else:
            return (-1)
