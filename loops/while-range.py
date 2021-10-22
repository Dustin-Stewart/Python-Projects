'''print('while stuff\n')

a=0
b=10
x=[a for a in range(b+1)]
y=x

print('x = ',x)
while a<=b:
    print('remove',x.pop(),x)
    a+=1
print('all gone')


print('Break and Continue')

while True:

    for i in y:
        if i == 5:
            continue
        print(y[i])
        if i==7:
            break

    break
'''

print('nested list example')

x=['big','small','bold','light','heavy']
y=['iron','silver','gold','platinum','diamond']

a=b=0

for i in x:
    for j in y:
        print(x[a],y[b])
        b+=1
    a+=1
    b=0
