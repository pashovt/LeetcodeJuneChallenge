"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact, digits = [1]*n, [1]*n
        for i in range(1, n):
            fact[i] = fact[i-1]*(i+1)
            digits[i] = i+1
            
        result = ""
        while len(result) < n-1:
            repeat = fact[-2]
            next_digit = (k-1)//repeat
            result += str(digits[next_digit])
            digits.pop(next_digit)
            fact = fact[:-1]
            k = k % repeat
            if k == 0:
                for i in range(len(digits)-1, -1, -1):
                    result += str(digits[i])
        if len(result) < n:
            result += str(digits[0])
            
        return result

Solution.getPermutation(3,3)
