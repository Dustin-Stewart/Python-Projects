print('various data types like lists, sets, etc\nlists are between [] and are mutable')

x= ['red','blue','green','yellow','black']
print('\nprint a list:\nx= [\'red\',\'blue\',\'green\',\'yellow\',\'black\']\nprint(x): ',x)


x= ['red','blue','green','yellow','black',3]
print('\ndifferent data types in one list:\nx= [\'red\',\'blue\',\'green\',\'yellow\',\'black\', 3]\nprint(x): ',x)

print('what type is the 3 in the list now?\nprint(type(x[5])):\n','x[5](',x[5],')is type',type(x[5]))

print('\nlist class methods:\n',dir(list))

print('\nlength = len():\n length of x =',len(x),'etc..')



print('\nTuples are immutable lists and are between () (read only list)')
print('tuples methods:\n',dir(tuple))

x={'number':1, 'name':'blue','age':200.5}
print('\nDictionaries are mapped lists with key/pair values and are between {}.\nkeys are strings and are seperated from values with a \':\'.\n\ne.g.: x={\'number\':1, \'name\':\'blue\',\'age\':200.5}')
print('access a value in the dictionary: x[\'name\'] =',x['name'])
print('\nreassign name:\nx[\'name\']=\'orange\'')
x['name']='orange'
print(x)

x['new element'] = 'a new element'
print('\nadd an element:\nx[\'new element\'] = \'a new element\'',x)

print('\ndictionary methods:\n',dir('dictionary'))
