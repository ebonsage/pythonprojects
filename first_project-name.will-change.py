#! python 3
#coreyjones
import os, sys, requests, bs4, re, pprint


mainUrl = 'https://xkcd.com/2079/'
downloadFolder = 'C:\\picbot'
swapFile = '%s\\swap.txt' % (downloadFolder)
url = []

if not os.path.exists(downloadFolder):
    os.makedirs(downloadFolder)

assert os.path.isdir(downloadFolder), 'Download folder is missing! ' + str(downloadFolder)

os.chdir(downloadFolder)
pwd = os.getcwd()   
pprint.pprint(pwd)


    
    
#----------------------------------------------------------------------
def snapPage(url):
    """Pull current page and save to a file"""
    res = requests.get(mainUrl)
    res.raise_for_status()         
    #if not os.path.exists(swapFile):
        #swap = open(swapFile, mode='w+')
        #swap.write('BEGIN SWAPFILE' + '\n\n\n\n')
        #swap.close()

    #swap = open(swapFile, mode='wb')
    #for chunk in res.iter_content(100000):
        #swap.write(chunk)
    #swap.close()
    #div id="comic"
    #dirtyFile = open(res.text, mode='r')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    csoup = str(soup.select("[id~=comic]"))
    pprint.pprint(csoup)
    
    dsoup = csoup.split(" ") #create a list
    picName = dsoup[3]
    rlink = dsoup[4]
    print("picName is: " + picName)
    print("rlink is: " + rlink)
    #cleanFile.close()
    #print(csoup)
    #return elems[0].text.strip()
    rough = re.compile(r'("([^"]*)")')
    #r'((src=")([^ ])+)'
    smooth = rough.findall(rlink)
    print(type(smooth))
    print(smooth)
    rsmooth = list(smooth)
    print(rsmooth)
    print(rsmooth[1])
    
    #smoother = smooth[34:67]
    #pprint.pprint(smoother)
    #loot = smooth.replace('"', "")
    #print(smoother)
    #return smooth



        

snapPage(mainUrl)
#beginDownload.parsePage()





#firgure html for image
#requst to downlaod the image
#parse for forward or back link
#grab url from previous page
#goto that new url and repeat
