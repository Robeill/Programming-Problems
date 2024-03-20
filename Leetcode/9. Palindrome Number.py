class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = x
        reverse = 0
        while num > 0:
            lastdigit = num % 10
            reverse = reverse * 10 + lastdigit
            num = num / 10
        if reverse == x:
            return True
        else:
            return False
    # return str(x) == str(x)[::-1] # This would be the one liner solution
        