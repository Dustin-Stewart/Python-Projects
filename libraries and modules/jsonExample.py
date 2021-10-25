import json

x = {'name':'alex', 'age':120 , 'job':'developer'}
print(x)
y = json.dumps(x)

file = open('jsonEx.json', 'w')
file.write(y)
file.close()

file = open('jsonEx.json', 'r')
x= file.read()
print(x)
