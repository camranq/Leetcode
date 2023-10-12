class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

    def isPalindrome2(self, x: int) -> bool:
        pass