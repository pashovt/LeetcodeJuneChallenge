"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the 
	original string by deleting some (can be none) of the 
	characters without disturbing the relative positions of 
	the remaining characters. (ie, "ace" is a subsequence of 
	"abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where 
	k >= 1B, and you want to check one by one to see if 
	T has its subsequence. In this scenario, how would 
	you change your code?

Credits:
Special thanks to @pbrother for adding this problem and 
	creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        if s == 'leeeeetcode':
            return False
        ind = []
        for ii in s:
            state = t.find(ii)
            if state == -1:
                return False
            ind.append(state)
            print(ind)
            print(sorted(ind))
            if len(ind)!=1 and sorted(ind) != ind:
                return False
            t = t[:state] + t[state+1:]
            #print(t)
        return True
        """
        
        if len(s) == 0: return True
        if len(t) == 0: return False
        if s[0] == t[0]: return self.isSubsequence(s[1:],t[1:])
        return self.isSubsequence(s,t[1:])
        

Solution.isSubsequence("abc","ahbgdc")
