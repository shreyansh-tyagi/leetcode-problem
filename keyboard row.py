'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
 

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 


'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1={'q','w','e','r','t','y','u','i','o','p'}
        r2={'a','s','d','f','g','h','j','k','l'}
        r3={'z','x','c','v','b','n','m'}
        a=[]
        for i in words:
            b=set(i.lower())
            if (b&r1==b)or(b&r2==b)or(b&r3==b):
                a.append(i)
        return a        