#raw_input('dsfsg')
a = []
v = [1, 2, 4, 5]
f = open('workfile.txt','w+') #by default text file
for i in range(10):
    a.append(i)
    f.write('row_number is:{0}'.format(i) + '\n')
    f.writelines(v)
f.close()

#need to read more!