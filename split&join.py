#import string
#string join ()

q = 'td'.join(['1', '2', '3', '4'])
q2 = ''.join(['1', '2', '3', '4'])
print(q)
print(q2)

q3 = q2.split('-s',2)
print(q3)

s='''
multi
string
test
'''
print(s)
print(s.splitlines())