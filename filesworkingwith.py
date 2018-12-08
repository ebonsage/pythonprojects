import os, pprint
#coreyjones

########################################################
pprint.pprint("THIS IS THE START TO WORKING WITH FILES")


bump = 'C:\\pytemp\\examplefile.txt'

pprint.pprint(os.path.isfile(bump))
helloFile = open(bump)

tamp = helloFile.read()
pprint.pprint(tamp)
helloFile.close()
pprint.pprint(tamp)

stomp = 'C:\\pytemp\\newexmp.txt'
cramp = open(stomp, 'a+')
pprint.pprint(cramp)
cramp.write('Hello!!!!!!!!!!!' + '\n')
# helloFile = open('c:\\users\\someone\\hello.txt', 'w' or 'a' or '+'
cramp.close()
cramp = open(stomp, 'r+')

pprint.pprint(cramp.read())
