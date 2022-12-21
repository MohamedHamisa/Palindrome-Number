import math 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        orig = x
        back_x = 0
        while x > 0:
            back_x = (back_x * 10) + (x % 10)
            x = x // 10
        return orig == back_x

'''
when you compute x % 10 you return the reminder which is the last digit of the current number x
when you do back_x = (back_x * 10) + (x % 10) you shift the current last digit forward and then add x % 10 to the end of the number.
and of course, every step you perform x = x // 10 which cuts off the last digit from the number so you can access the next "last digit"
'''
