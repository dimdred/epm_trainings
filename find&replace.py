s = '12345 1 2 3 4 5'
print(s.index(' 2'))
print(s.find('7'))
#print(s.index('7')) -- error

s1 = 'aaaa'
print(s1.count('aa'))
print(s1.count('aa',1)) #move right to 1 symbol
s2 = s1.replace('aa','123', 1) #onlu for 1 element
print(s2)