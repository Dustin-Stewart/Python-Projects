from dice import x
import random

inp = input('Roll the dice? (y/n)\n')

while (inp == 'y'):
    print('\n',x[random.randrange(0,6)])
    inp = input('Roll the dice? (y/n)\n')
    if (inp != 'y'):
        print('\ngood game')
