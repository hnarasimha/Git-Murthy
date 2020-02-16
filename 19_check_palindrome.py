'''
check if palindrome can be formed
'''

def check_palindrome(s):
    s_dict = dict()
    for t in s:
        ch = t.lower()
        if ch not in s_dict.keys():
            s_dict[ch] = 1
        else:
            s_dict[ch] += 1
    print ("count of each characters :",s_dict)
    count = 0
    for k in s_dict.keys():
        if s_dict[k] > 1 and s_dict[k] % 2 == 0:
            continue
        else:
            if count != 1:
                count = 1
            else:
                return (False)
    if count ==  1 or count == 0:
        return (True)
    else:
        return(False)


s = 'Repaperadz'
print (check_palindrome(s))