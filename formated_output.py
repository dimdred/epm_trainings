print('test string! 1 + 2 ={0}'.format(1+2))
print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc')) #unpacking argument sequence
print('{0} {1}{0}'.format('abra','cad'))

l = [1, 2, 3]
#print('{1}.{2}'.format(l)) #error 3 elements
print('{1}.{2}'.format(*l)) #sequence of arguments
print('{1:#X}.{2}'.format(*l)) #sequence of arguments

print('Coordinates: {latitude}, {long}'.format(latitude ='37.24N', long = '115.81W'))
coord = {'latitude': '37.24N', 'long': '115.81W'}
print('Coordinates: {latitude}, {long}'.format(**coord))
cord = (3,5)
print('x:{0[0]}; y:{0[1]}'.format(cord))

print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))

#import datetime
#print(d = datetime.datetime())

print('%+3d %s' %(1,2))
print('%+10f %s' %(1,2))
d = {'key1':1, 'key2':2}