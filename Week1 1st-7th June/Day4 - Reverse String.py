"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Hint 1:
The entire logic for reversing a string is based on using the opposite directional two-pointer approach!

"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # test case - ["h","e","l","l","o"]
        # first method - bacis python inbuild list manipulation
        # computional time - 56ms
        s.reverse()
        
        
        """
        # second method - simple list manipulation with insert and pop
        # computional time - 40ms
        for ii in range(0, len(s)):
            s.insert(ii, s[len(s)-1])
            s.pop()
        """     
        
        # 2.1 method - shortened version of the second method with 
        # simultaneously removing the last characted and then adding 
        # it at the desired postion
        # computional time - 56ms
        """
        for ii in range(0, len(s)):
            s.insert(ii, s.pop())
        """
        
        # third method - list comprehension with lambda function
        # computional time - 86ms
        """
        annfunc = lambda ind: s.insert(ind, s.pop()) 
        [annfunc(ind) for ind in range(0, len(s))]
        """

Solution.reverseString(["h","e","l","l","o"])
