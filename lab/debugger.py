#! python3
import random
import os

#coreyjones

def blahBlah():
    print('blah')
    print('blah')
    print('blah')
    moreBlah()
    print('blah')
    print('blah')
    print('blah')
    moreBlah()
    print('blah')
    print('blah')
    print('blah')

def moreBlah():
    print('more blah')
    print('more blah')
    print('more blah')

#blahBlah()


heads = 0

for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')

print('Heads came up ' + str(heads) + ' times.')



    
        
        
    
    
















#print('Enter the first number to add:')
#apple = 9
#rapp = "comodod"
#first = int(input())
#print('Enter second number to add:')
#second = input()
#print('Enter the third number to add:')
#third = input()
#print('The sum is ' + first + second + third)




