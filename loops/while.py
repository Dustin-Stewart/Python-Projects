print('while stuff\n')

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
