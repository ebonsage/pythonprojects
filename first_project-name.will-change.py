#! python 3
#coreyjones
import os, sys, requests, bs4, re, pprint


mainUrl = 'https://xkcd.com/730/'
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

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    csoup = str(soup.select("[id~=comic]"))
    pprint.pprint(csoup)
    
    dsoup = csoup.split(" ") #create a list
    picName = dsoup[3]
    rlink = dsoup[4]
    pic = picName.replace('"', '')
    print("picName is: " + pic)
    print("rlink is: " + rlink)

    rough = re.compile(r'("([^"]*)")')
    smooth = rough.findall(rlink)
    rsmooth = list(smooth)
    
    for i in smooth:
        newList = list(i)

    print(newList[1])
    url = newList[1]
    return pic, url
        

snapPage(mainUrl)
#beginDownload.parsePage()





#firgure html for image
#requst to downlaod the image
#parse for forward or back link
#grab url from previous page
#goto that new url and repeat
