print('example error: division by zero')

def div(a=int(input('enter an int')),b=int(input('enter an int'))):
    if(b==0):
        return 'division by zero, exiting...'
    else:
        return str(a/b) 
print(div())
