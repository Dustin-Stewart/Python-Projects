print('For loops')

print('using list comprehension to create a list of numbers 1-10\n list comprehension Syntax -  [(expression) (context)]')
number = [i+1 for i in range(10)]
buff = number
print(number)

print('\niterative print')
for item in number:
    print(item-1)

print('\nreplace the items with user input using list comprehension')

number = [input('replace '+str(item)+' with: ') for item in number]
deltas = {str(buff[i]):str(number[i]) for i in range(len(number))}
print(deltas)
