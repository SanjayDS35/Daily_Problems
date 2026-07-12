# Leetcode-9 Palindrome Number [EASY] | Date:12-07-2026

'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1

'''

# Using String slicing 

class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        return s==s[::-1]

# Using mathematical expression

'''
class Solution(object):
    def isPalindrome(self, x):
        n=x
        rev=0
        if x>=0:
            while(x!=0):
                rev=(rev*10)+x%10
                x//=10
            return rev==n
        else:
            return False

'''
