'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.

'''
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c,b=0,[]
        if len(words)>=1 and len(words)<=1000:
            for i in words:
                if len(i)>=1 and len(i)<=100:
                    for j in range(len(i)):
                        if i[j] in chars:
                            c+=1
                        else:
                            break
                    if c==len(i):
                        b.append(len(i))
                        c=0
                else:
                    return 0
        else:
            return 0
        return sum(b)        
                    
                    