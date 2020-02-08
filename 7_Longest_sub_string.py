'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


'''

def lengthOfLongestSubstring(s):
    temp=''
    string=''
    for i in s:
        if i not in temp:
            temp+=i
            if len(string)<len(temp):
                string=temp
        else:
            idx=0       
            for j in temp:
                idx=temp.find(i)
                break
            temp=temp[idx+1:]
            temp+=i
            if len(string)<len(temp):
                string=temp
            
    return(len(string))

s="abcabcbb"
print(lengthOfLongestSubstring(s))


