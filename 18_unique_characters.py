
def uniqueLetterIn_string (s):
	for i in range(len(s)):
		if s[i] not in (s[0:i]+s[i+1:len(s)]):
			return ("unique string")
		else:
			return("not unique string")
s = "abc"
print (uniqueLetterIn_string (s))