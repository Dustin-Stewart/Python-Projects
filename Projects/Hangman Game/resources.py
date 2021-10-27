import random

images = ['''-----''',

          '''-----\n 0''',

          '''-----\n 0\n |''',

          '''-----\n 0\n |\n/''',

          '''-----\n 0\n |\n/ \ ''',

          '''-----\n\\0\n |\n/ \ ''',

          '''-----\n\\0/\n |\n/ \ ''',

          '''-----\n\\0/ |\n |\n/ \ ''',

          '''-----\n\\0/_|\n |\n/ \ ''',

          '''-----\n 0_|\n/|\ \n/ \ ''']

def wordState(guess,word):
    if guess in word:

        return

def getWord():
    dic = list()
    with open('words.txt') as file:
        while (line := file.readline().rstrip()):
            if len(line) == 10 and '\'' not in line:
                dic.append(line)
    print('choosing a word from',len(dic),'words')
    word = dic[random.randrange(0,len(dic))]
    return word

def play(word):
    print(word)
    for i in range(10):
        guess = input('\nguess a letter: \n')
        if guess in word:
            print ('guess in word\n',i+1)
            i-=1
        else:
            print('wrong',i+1)
            print(images[i])
    print('\ngame over')
