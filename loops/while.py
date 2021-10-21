print('while stuff\n')

a=0
b=10
x=[a for a in range(b+1)]
print('x = ',x)
while a<=b:
    print('remove',x.pop(),x)
    a+=1
print('all gone')
