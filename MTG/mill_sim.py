import random
import argparse
import itertools

parser = argparse.ArgumentParser(description='Simulates Undead Alchemist + Altar of Dementia Combo')
parser.add_argument('--decksize',  dest="deck_size", type=int, help='The Size of The Deck to be Milled')
parser.add_argument('--creatures', dest="creatures", type=int, help='Number of Creatures on The Deck')
parser.add_argument('--power', dest="power", type=int, default=2, help='Power of each Zombie (default: 2)')
parser.add_argument('--iterations', dest="iterations", type=int, default=1, help='Number of iterations (default: 1)')
parser.add_argument('--full', action='store_const', dest="full",const=True,  default=False, help='Should generate full data (default: false)')


args = parser.parse_args()

#print(args)

def simulateCombo(decksize, creatures, power):
    deck = [1]*creatures
    deck.extend([0]*decksize)
    random.shuffle(deck)
    
    zombies= 1
    milled = 0
    
    while zombies > 0:
        _z = 0
        for i in range(power):
            try:
                _z += deck.pop()
            except:
                return(decksize)
        zombies = zombies - 1 + _z
        milled += 2
    return milled


#print("You milled %i from a %i card deck with %i creatures" % (simulateCombo(args.deck_size, args.creatures, args.power), args.deck_size, args.creatures))
def singleSimulation():
    print("deck,#creature,power,milled")
    simulateIterations(args.iterations, args.deck_size, args.creatures,args.power)

def simulateIterations(iterations, ds, creatures, power):
    for i in range(iterations):
        print("%i,%i,%i,%i" % (ds, creatures, power, simulateCombo(ds, creatures, power)))

def generateData(iterations):
    print("deck,#creature,power,milled")
    powers = [2,3,4,5]
    sizes = [100]
    creatures = [10,20,30,40]
    for ds in sizes:
        for c in creatures:
            for p in powers:
                simulateIterations(iterations,ds,c,p)
                
if args.full:
    generateData(args.iterations)
else:
    singleSimulation()
