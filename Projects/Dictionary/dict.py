from PyDictionary import PyDictionary
dictionary=PyDictionary()

def getDef(x):
    while True:
        if x==('x!'):
            print('Thanks for running me!\n')
            exit(0)

        if (dictionary.meaning(x,True)):
            define = dictionary.meaning(x)
            print('\n'+x+':')
            for k,v in define.items():
                i=1
                print('\n',k,': ')
                for item in v:
                    print (i,') ',item)
                    i+=1
            x = input('\nEnter your search term here, or enter \'x!\' to exit: ')
        else:
            print('\n',x,' is not a word')
            x = input('\nEnter your search term here, or enter \'x!\' to exit: ')
