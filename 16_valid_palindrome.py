'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false


'''

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s_copy = ''
    for i in s:
        if i.isalnum():
            s_copy += i.lower()
    print ("s_copy",s_copy)
    if s_copy == s_copy[::-1]:
        return (True)
    else:
        return(False)

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))