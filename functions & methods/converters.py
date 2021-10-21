print('celcius to farenheit')
c= int(input('Enter the temp in celcius'))
f= (9/5)*c+32

print(f)

s = int(input('enter the seconds'))
m = int(input('enter the minutes'))

h = m/60 + s/3600
print(h)


print('\nnow as a function')

print('C to F\n')
def c2f(c=float(input('enter the degrees in C: '))):
    return str((9/5)*c+32)+'F'
print(c2f())


print('\nS + M to Hours')
def hours(s = int(input('enter the seconds')),m = int(input('enter the minutes'))):
    return str(s)+' seconds and '+str(m)+' minutes gives '+str(m/60 + s/3600)+' hours'
print(hours())

print('\nnow as a lambda')

c2fl = lambda c: print(str((9/5)*c+32)+'F')
c2fl(c=float(input('enter a temp in C:')))
