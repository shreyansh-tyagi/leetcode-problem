'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        f=strs[0]
        l=strs[len(strs)-1]  
        s=""
        for i in range(len(min(f,l))):
            if l[i]==f[i]:
                s+=l[i]
            else:
                break
        return s
        