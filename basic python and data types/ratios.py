'''piece count to cost ratio calculator for finding the best price on bulk gum'''
ratios = {'n':input('Gum name one: '),'a':float(input('input pieces: ')),'b':float(input('input price: ')),'n2':input('Gum name 2: '),'c':float(input('input pieces: ')),'d':float(input('input price: '))}

def computeBetterDeal():
    print('\nthe best deal is on:')
    if(ratios['a']/ratios['b'] > ratios['c']/ratios['d']):
        return ratios['n']
    elif(ratios['a']/ratios['b'] == ratios['c']/ratios['d']):
        return 'same value'
    else:
        return ratios['n2']

print(computeBetterDeal())
