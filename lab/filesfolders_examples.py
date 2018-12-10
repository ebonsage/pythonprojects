import os, pprint, random, shelve, shutil, send2trash
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
        #os.makedirs(mek)



########################################################
pprint.pprint("shelve examples -->")

os.chdir('c:\\delicious')

shellFile = shelve.open('mydata')

#store data or write to file
shellFile['cats'] = ['zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo' ]

shellFile.close()

shellFile = shelve.open('mydata')

#grab data
pprint.pprint(shellFile['cats'])

shellFile.close()

shellFile = shelve.open('mydata')
pprint.pprint(list(shellFile.keys()))
pprint.pprint(list(shellFile.values()))
shellFile.close()


########################################################
pprint.pprint("shutils examples -->")

os.chdir('c:\\delicious')
#shutil.copy('c:\\delicious\\moving.txt', 'c:\\delicious\\cate\\pie\\moved.txt') 
#to copy a file and rename it specify the file name in the dest.

#shutil.move('c:\\delicious\\cate\\moved.txt', 'c:\\delicious\\cate\\pie')
#move file and rename files

#send2trash.send2trash('c:\\delicious\\cate\\pie\\moved.txt')

#shutil.copytree('c:\\delicious', 'c:\\delicious.bak')
#copy a folder and its contents.



########################################################
pprint.pprint("deleting files and folders examples --> ")


os.chdir('c:\\delicious')
pprint.pprint(os.getcwd())
#os.unlink('C:\delicious.bak\\cate\\bacon.txt') #delte fiels
#os.rmdir('C:\delicious.bak\\cate\\pie\\cherry') 
#removes an empty directory


#shutil.rmtree('c:\\delicious')
#remove files and folders

for filename in os.listdir():
    if filename.endswith(''):
        #os.unlink(filename)
        pprint.pprint(filename)
        

######### send2trash
        
#send2trash.send2trash('c:\\delicious\\cate\\pie\\moving.txt')

########################################################
pprint.pprint("walking the directory tree examples -->")


takp = os.walk('c:\\delicious')
pprint.pprint(takp)

for folderName, subfolders, fileName in takp:
    pprint.pprint('The folder is ' + str(folderName) + ' foldername.')
    pprint.pprint('The folder is ' + str(subfolders) + ' subfolders.')
    pprint.pprint('The folder is ' + str(fileName) + ' filename.')
    print()
    print()
    print('The folder is ' + folderName)
    print('The subfolder in ' + folderName + ' are:' + str(subfolders))
    print('The filenames in ' + folderName + ' are:' + str(fileName))
    
    for subfolder in subfolders:
        print(subfolder)
        #os.unlink(subfolder) #delete all files in that folder
        
        for subfolder in subfolders:
            if 'fish' in subfolder:
                #os.rmdir(subfolder)
                print('rmdir on ' + subfolder)
                
        for file in fileName:
            if file.endswith(''):
                gone = os.path.join(folderName, file + '.backup')
                #shutil.copy(os.path.join(folderName, file), gone )
                pprint.pprint('Copying ' + file + ' to: ' + gone)
                
        
        
#####
print()

