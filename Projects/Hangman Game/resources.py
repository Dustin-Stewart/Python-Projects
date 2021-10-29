import random

images = [''' \n\n\n''',

          '''-----\n\n\n''',

          '''-----\n 0\n\n''',

          '''-----\n 0\n |\n''',

          '''-----\n 0\n |\n/''',

          '''-----\n 0\n |\n/ \ ''',

          '''-----\n\\0\n |\n/ \ ''',

          '''-----\n\\0/\n |\n/ \ ''',

          '''-----\n\\0/ |\n |\n/ \ ''',

          '''-----\n\\0/_|\n |\n/ \ ''',

          '''-----\n 0_|\n/|\ \n/ \ ''']


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
    word = list(word)


    def wordState(guess):
        display = ['-'*len(word)]
        if guess not in word:
            return ''.join(display)
        else:
            for i in range(len(word)):
                print(guess,word[i+1])
                if guess == word[i]:
                    display[i] = guess
                    print('display')
            return ''.join(display)

    tries = len(word)
    state = None
    while tries !=0:
        guess = input('\nguess a letter: \n')
        if guess in word:
            if state == None:
                print('\nnice\n')
            else:
                print ('\nnice.\n',state)
        else:
            print('\nwrong')
            tries-=1
            print(state := images[len(word)-tries])
        print(wordState(guess))
    print('\ngame over')
