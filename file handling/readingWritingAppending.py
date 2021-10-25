'''file = open('filePath', arg) or close
r for read
w for write
a for appending
+ for reading and writing
a+ for appending and reading
x for explicit creation (error if file exists)
'''

def writeBack():
    file = open('test.txt', 'r')
    x = file.read()
    print('\n',x)
    file.close()

'''reading '''
file = open ('test.txt' , 'r')
x = file.read()
print(x)
file.close()

'''new file'''
file = open('test2.txt' , 'w')
file.close()

'''write to a file'''
file = open('test.txt', 'w')
file.write("pink")
file.write('\nblue')
file.close()

writeBack()

x=['red','green','black','yellow']
file = open('test.txt','w')
for i in x:
    file.write(i+'\n')
file.close()

writeBack()

file = open('test.txt','a')
file.write('purple\n')
file.write('teal\n')
file.close()

writeBack()
