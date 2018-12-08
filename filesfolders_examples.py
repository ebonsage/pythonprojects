import os, pprint, random
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
gpwd2 = os.getcwd()
pprint.pprint(gpwd2)


#absolute path
abs = os.path.abspath('spam.png')
pprint.pprint(abs)


os.chdir('c:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\')
gpwd3 = os.getcwd()
pprint.pprint(gpwd3)
pprint.pprint(os.path.abspath('..\\..\\spam.png'))
gpwd4 = os.getcwd()
pprint.pprint(gpwd4)

pprint.pprint(os.path.isabs('c:\\ProgramData\\Microsoft\\Windows'))  #check for abs path returns T or F
pprint.pprint(os.path.relpath('c:\\folder1\\folder2\\folder3\\folder4\\spam.png', 'c:\\folder1\\folder2'))


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

pprint.pprint(os.path.dirname('c:\\folder1\\folder2\\spam.txt'))
pprint.pprint(os.path.basename('c:\\folder1\\folder2\\spam.txt'))



########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

pprint.pprint(os.path.exists('c:\\folder1\\folder2'))
pprint.pprint(os.path.exists('C:\\Windows\\System32\\drivers\\etc\\hosts'))
pprint.pprint(os.path.isfile('C:\\Windows\\System32\\drivers\\etc\\hosts'))
pprint.pprint(os.path.isdir('C:\\Windows\\System32\\drivers\\etc'))


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")


pprint.pprint(os.path.getsize('C:\\Windows\\System32\\drivers\\etc\\hosts'))
pprint.pprint(os.path.getatime('C:\\Windows\\System32\\drivers\\etc\\hosts'))


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

sp = 'C:\\Windows\\System32\\drivers\\etc'
fn = 'hosts'
cp = 'C:\\Windows\\System32\\drivers\\etc\\hosts'

pprint.pprint(os.listdir(sp))
totalSize = 0
for filename in os.listdir(sp):
    pprint.pprint(filename)
    if not os.path.isfile(os.path.join(sp, filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(sp, filename))
    pprint.pprint(totalSize)

pprint.pprint(os.path.join(sp, fn))

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

cdir = 'c:\\delicious\\cate\\pie\\cherry'



if os.path.isdir(cdir):
    addran = random.randint(1, 99999999)
    #addran = 45895498
    pprint.pprint(addran)
    mek = os.path.join(cdir, str(addran))
    if os.path.isdir(mek):
        pprint.pprint('File Exists')
    else:
        pprint.pprint(mek)
        os.makedirs(mek)





