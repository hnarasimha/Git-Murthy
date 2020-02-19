'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


'''
import math
def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        def number_of_digits(n):
            number = 0
            while(n):
                    n = int(n/10)
                    number += 1
            return (number)


        reverse_number = 0
        abs_x = abs(x)
        while (abs_x):
                digit = abs_x % 10
                reverse_number += digit * (10 ** (number_of_digits(abs_x) - 1))
                abs_x = int(abs_x/10)
        
        
        if abs(x) == x and reverse_number < (2 ** 31 -1):
            return reverse_number
        elif abs(x) != x and (reverse_number * -1) > (-1 * 2 ** 31):
            return reverse_number * -1
        else:
            return(0)


x = -120
print(reverse(x))

        
