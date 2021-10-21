x = 'is'
y = 'my'
z = 'name'

print('x = is\ny = my\nz = name')

c=x+y+z
print('\nc=x+y+z\nc=',c)
c=x+' '+y+' '+z
print('\nc=x+\' \'+y+\' \'+z\nc=',c)

x= 34
y= 'dustin'
z= 'my name is {} and my age is {}'.format(y, x)
print('\nmore dynamically (bracket delimiter):\nx= 34\ny= dustin\nz= \'my name is {} and my age is {}\'.format(y, x):\n',z)

z= 'my name is {1} and my age is {0}'.format(y, x)
print('\nswitch up more specifically (indexing):\nx= 34\ny= dustin\nz= \'my name is {1} and my age is {0}\'.format(y, x):\n',z)

z= f'my name is {y} and my age is {x}'
print('\nmore succinctly (formatted string):\nx= 34\ny= dustin\nz= f\'my name is {y} and my age is {x}\':\n',z)

c = ['34', 'dustin']
z= f'my name is {c[1]} and my age is {c[0]}'
print('\nindexing a list:\nx=[\'34\', \'dustin\'] \nz= f\'my name is {x[1]} and my age is {x[0]}\'\n',z)
