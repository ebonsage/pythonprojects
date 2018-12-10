#! python 3
#coreyjones
import os, sys, requests, bs4, re, pprint


mainUrl = 'https://xkcd.com/2058/'
downloadFolder = 'C:\\picbot'
swapFile = '%s\\pic_names.txt' % (downloadFolder)
url = []

if not os.path.exists(downloadFolder):
    os.makedirs(downloadFolder)

assert os.path.isdir(downloadFolder), 'Download folder is missing! ' + str(downloadFolder)

os.chdir(downloadFolder)
pwd = os.getcwd()   
pprint.pprint(pwd)

if not os.path.exists(swapFile):
    swap = open(swapFile, mode='w+')
    swap.write('BEGIN DOWNLOAD LOG' + '\n\n\n\n')
    swap.close()
    
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
    #print("picName is: " + pic)
    #print("rlink is: " + rlink)

    regExUrl2Filename = re.compile(r'("([^"]*)")')
    findLink = regExUrl2Filename.findall(rlink)
    
    for i in findLink:
        newList = list(i)

    #print(newList[1])
    xurl = newList[1]
    
    url = 'https:' + xurl
    print(pic, url)
    
    #return pic, url
        

#----------------------------------------------------------------------
def downLoadPic(pic, url):
    """Download pic to hdd"""
    
    regexFileName = re.compile(r'((?=\w+\.\w{3,4}$).+)')
    xfileName = regexFileName.search(url)
    fileName = xfileName.group()
    
    #r = requests.get(url, stream=True)
    #if r.status_code == 200:
        #with open(fileName, 'wb') as f:
            #for chunk in r:
                #f.write(chunk)
                
    logDownLoadList = open(swapFile, mode="a+")
    logDownLoadList.write(pic + '\t' + url + '\n')
    logDownLoadList.close()
    
        
        
#----------------------------------------------------------------------
def grabPrevURL(url):
    """Grab the Next URL"""

    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    prevURL = str(soup.select("ul.comicNav"))

    #pprint.pprint(prevURL)
    
    aTags = soup.find_all(re.compile("^a"))
    bTags = aTags[7]
    
    pprint.pprint(bTags)
    pprint.pprint(type(bTags))
    test = str(bTags)
    pprint.pprint(test)
    regexPreUrl = re.compile(r'(\/\d{1,8}\/)')
    xPreUrl = regexPreUrl.search(test)
    print(xPreUrl)
    preUrl = xPreUrl.group()    
    pprint.pprint(preUrl)
    print('https://xkcd.com' + preUrl)
    return 'https://xkcd.com' + preUrl



#firgure html for image
#requst to downlaod the image
#parse for forward or back link
#grab url from previous page
#goto that new url and repeat


#downLoadPic(snapPage(mainUrl))
#snapPage(mainUrl)
#downLoadPic("firstPic", "http://imgs.xkcd.com/comics/circuit_diagram.png")
grabPrevURL(mainUrl)
