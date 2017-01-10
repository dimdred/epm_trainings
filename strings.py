s = ' str /"/" test'
print(s)
s1 = """test "
alias"
"""
print(s1)
s2 = ''' Multi
line
text
'''
print(s2)

#modify string
print(s.strip('s'))

#add null element to string before find end
ss = 'sd0'
print(ss.zfill(10))

#translation decode/encode
#a = 'AB' #on rus
#print(a.decode('utf-8'))

print(ss.isalnum())
print(ss.isalpha())