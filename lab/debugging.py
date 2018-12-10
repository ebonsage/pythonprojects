import os, traceback, pprint



#raise Exception('There is a problem here.')
#create my own custom exceptions that are rasied.

smg = """

^^^^^^^^^^^^^^^^^^
^                ^
^                ^
^                ^
^^^^^^^^^^^^^^^^^^

"""


########################################################
pprint.pprint("execeptions examples --> ")



os.chdir('c:\\delicious')



def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol", needs to be a string of length 1')
    if (width <= 2) or (height <= 2):
        raise Exception('"symbol" needs both w & l to be a number greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
    
    
boxPrint('*',  15, 5)
boxPrint('O', 4,3)


#try:
    #raise Exception('This is the error message.')
#except:
    #errorFile = open('error_log.txt', 'a')
    #errorFile.write(traceback.format_exc())
    #errorFile.close()
    #print('The traceback info was written to error_log.txt')
    

########################################################
pprint.pprint("assertions (asser) examples --> ")

#assert False, 'This is the error message'


market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        print(key + ' ' + intersection[key])
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
        print(key + ' ' + intersection[key])
        #assert 'red' in  intersection.values(), 'Neither light is red! ' + str(intersection)
        #sanity check for errors that are programmatically correct
        #I assert that this condition always holds True, and if not, there is a bug

pprint.pprint(market_2nd)
switchLights(market_2nd)
pprint.pprint(market_2nd) 