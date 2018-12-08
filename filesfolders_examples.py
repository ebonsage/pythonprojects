import os, pprint
#coreyjones

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

expath = os.path.join('folder1', 'folder2', 'folder3', 'filename.txt')
pprint.pprint(expath)

#current working directory os.getcwd()

pwd = os.getcwd()
pprint.pprint(pwd)


#change dir os.chdir('c:\\')  works on the terminal
gpwd = os.getcwd()
pprint.pprint(gpwd)
os.chdir('c:\\')
pprint.pprint(gpwd)



########################################################
#pprint.pprint("THIS IS A NEW INSTANCE BELOW")