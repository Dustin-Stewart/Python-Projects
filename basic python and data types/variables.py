print("section 1/nvariable assignment and overwriting")
x="dev"
x = 5
y=6
z=5+6
c=x+y
print(x)
print(5)
print(z,c)

print("\nsection 2 /n order of operations preserved in python")

x = 3+5*6
print(x)


print("\nsection 3\n casting")

x=2

print("x =",x)
print("type of x =",type(x))

print("\nconvert to float")
print("float(x) =",float(x))
print("type of x =",type(x))

print("didnt work try this:\nx = float(x)")
x = float(x)
print("type of x =",type(x))
print("x =",x)

print("change it back\nx = int(x)")
x = int(x)
print("type of x =",type(x))
print(x)

print("section 4\nStrings")

print("\nNo char type in python, all single character values are considered strings")

a="a"
print("a =",a)
print("type of a =",type(a))

a="2"
print("a =",a)
print("type of a =",type(a))

print('\ndouble quotes and single quotes do the same thing')


print('\nmultiple assignment: assign single value to multiple variables\nm=a=n=y=\'one value\'')
m=a=n=y='one value'
print('m =', m)
print('a =', a)
print('n =', n)
print('y =', y)

print('\ndelete references with del()\ndel(m)')
del(m)
print(m)
