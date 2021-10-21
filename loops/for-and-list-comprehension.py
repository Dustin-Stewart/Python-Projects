print('For loops')

print('using list comprehension to create a list of numbers 1-10\n list comprehension Syntax -  [(expression) (context)]')
number = [i+1 for i in range(10)]
buff = number
print(number)

print('\niterative print')
for item in number:
    print(item-1)

print('\nreplace the items with user input using list comprehension, and track them with a dictionary')

number = [input('replace '+str(item)+' with: ') for item in number]
deltas = {str(buff[i]):str(number[i]) for i in range(len(number))}
print(deltas)

print('\nnow some string stuff')
for i in 'dictionary':
    print(i)

print('''\nalso the notion of for-else where we search for something in a set and then if we dont find it
        or completely index the set without finding it we perform the else''')
