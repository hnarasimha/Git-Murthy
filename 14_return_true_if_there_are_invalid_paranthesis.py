def invalid_paranthesis(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == '(' or s_list[i] == '{' or s_list == '[':
            for j in range(i+1, len(s_list)):
                # if s_list[i] == '(' and s_list[j] == ')':
                #     s_list.pop(i)
                #     s_list.pop(j - 1)
                # if s_list[i] == '[' and s_list[j] == ']':
                #     s_list.pop(i)
                #     s_list.pop(j - 1) 
                # if s_list[i] == '{' and s_list[j] == '}':
                #     s_list.pop(i)
                #     s_list.pop(j - 1)

    if ('(' in s_list) or (')' in s_list) or ('[' in s_list) or (']' in s_list) or ('{' in s_list) or ('}' in s_list):
        return False
    else:
        return True
s="()"
print(invalid_paranthesis(s))