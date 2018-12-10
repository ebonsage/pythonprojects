import os, logging

os.chdir('c:\\delicious')


logging.disable(logging.DEBUG)
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#logging.DEBUG
#logging.INFO
#logging.WARNING
#logging.ERROR
#logging.CRITICAL


logging.debug('Start of Program')

def factorial(n):
    logging.warning('Start of factorial(%s)' % (n))
    total = 1
    logging.info('init var to = 1')
    for i in range(1, n + 1):
        logging.warning('+1 iteration')
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))



