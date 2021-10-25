import datetime

x=datetime.datetime.now()
print(x,'\n')

print('classes datetime:\n',dir(datetime))
print('\ndatetime class attributes:\n',dir(datetime.datetime))

print(x.month,' october')

d1 = datetime.datetime(2021,10,25,11,00,00)
d2 = datetime.datetime.now()

diff = d2-d1

print()
print(x.strftime('Today is %A, the %dth of %B and it has been exactly'),
                    diff.seconds//3600,'hours', diff.seconds//60%60,'minutes',
                    round((diff.seconds/3600)%1*60%1*60),
                    'seconds since 11 oclock on the 25th of October, 2021.')
