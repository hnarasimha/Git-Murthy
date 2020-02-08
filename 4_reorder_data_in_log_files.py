#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:36:24 2020

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

 

Constraints:

    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    logs[i] is guaranteed to have an identifier, and a word after the identifier.


@author: mharesam
"""

def reorderLogfiles (logs):
        let_logs = []
        dig_logs = []
        let_logs = [i for i in logs if i[-1].isalpha()]
        dig_logs = [i for i in logs if i[-1].isdigit()]
        let_logs_dict = {}
        for i in let_logs:
            temp = []
            temp = i.split(" ",1)
            if temp[0] not in let_logs_dict: 
                let_logs_dict[temp[0]] = temp[1]
            else:
                let_logs_dict[temp[0]+'#'] = temp[1]
        let_keys = sorted(let_logs_dict.keys(),key=let_logs_dict.get)
        final = []
        for i in let_keys:
            final.append(i.strip('#')+' '+let_logs_dict[i])
        final.extend(dig_logs)
        return(final)
        

logs=["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0", "m azv x f", "7e apw c y", "8 hyyq z p", "6 3272401", "c otdk cl", "8 ksif m u"]
print(reorderLogfiles(logs))
