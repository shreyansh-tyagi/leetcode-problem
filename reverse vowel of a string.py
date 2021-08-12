'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
Accepted

''''
class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        a,b=[],0
        for i in s:
            if i in v:
                a.append(i)
                s = s.replace(i,'$')

        for j in s:
            if j == '$':
                b-=1
                s = s.replace(j,a[b],1)

        return s