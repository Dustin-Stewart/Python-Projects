x=3
y=x
if (x==2):
    print('x == 2')

elif x>=y:print('as a lambda\nx >= y')

else: print('idk')

print('password practice')
pwd = 'pwd'
count = 0

while count <=4:
    tries = 5-count
    count+=1
    inp = input('\nenter the pwd\nremaining tries: '+str(tries)+'\n')

    if inp==pwd:
        print('thank you')
        exit(0)

    elif tries>2:
        print('try again')

    elif tries == 2:
        print('hint: the pwd is: \'pwd\'')

    else:
        print('try again later')


print('\nnesting\n')

x=y=3
z=4

if x==y:
    if x!=z:
        if y!=z:
            if z>x:
                print('x == y')
else:
    ('somethings wrong')
