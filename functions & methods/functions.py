a=3
b=2
c=a+b
print(c)

d=4
e=6
f=d+e
print(f)

print('now with a function')

def add(x,y):
    z = x + y
    return z

print(add(a,b),',',add(d,e))

print('\nnow take the input from the user')
a= int(input('enter the first int '))
b= int(input('enter the second int '))
print(add(a,b))

print('\ninitialize inside a param')

def mult(x=int(input('enter an int to double: ')),y=2):
    return x*y
print(mult())
