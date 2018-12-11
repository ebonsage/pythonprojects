#!/usr/bin/env python
#coding:utf-8
#coreyjones

"""
  Author: coreyjones  --<>
  Purpose: Download all pictures from https://xkcd.com and log each download
  Created: 12/10/2018
"""
import os, requests, bs4, re, logging

mainUrl = 'https://xkcd.com'
downloadFolder = 'C:\\picbot'
swapFile = '%s\\pic_names.txt' % (downloadFolder)
loggingFile = '%s\\DEBUGLog.txt' % (downloadFolder)

#----------------------------------------------------------------------
def main():
    """"""
    if not os.path.exists(downloadFolder):
        os.makedirs(downloadFolder)
        
    assert os.path.isdir(downloadFolder), 'Download folder is missing; doesn\'t exist: ' + str(downloadFolder)
    
    os.chdir(downloadFolder)
    pwd = os.getcwd()
    logging.info('PWD:  %s' % (pwd))

    if not os.path.exists(swapFile):  
        swap = open(swapFile, mode='w+')
        swap.write('BEGIN DOWNLOAD LOG' + '\n\n\n\n')
        swap.close()
    
    assert os.path.exists(swapFile), 'Download folder is missing; doesn\'t exist: ' + str(swapFile)
    
    if not os.path.exists(loggingFile):    
        swap = open(loggingFile, mode='w+')
        swap.write('BEGIN DEBUG LOG' + '\n\n\n\n')
        swap.close()
        
    assert os.path.exists(loggingFile), 'Download folder is missing; doesn\'t exist: ' + str(loggingFile)
        
    #logging.disable(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    #logging.basicConfig(filename=loggingFile, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    #logging.DEBUG
    #logging.INFO
    #logging.WARNING
    #logging.ERROR
    #logging.CRITICAL
    
            
#----------------------------------------------------------------------
def snapPage(url):
    """Pull current page"""
    
    res = requests.get(url)
    res.raise_for_status()         

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    csoup = str(soup.select("[id~=comic]"))
    logging.debug('csoup: %s' % (csoup))
    
    dsoup = csoup.split(" ") #create a list
    
    try:
        for i in range(len(dsoup)):
            #find link
            logging.debug('The contents of soup are: %s' % (dsoup))
            logging.debug('soup index %s: ' % (dsoup[i]))
            peek = dsoup[i]
            suffix = 'png"'
            suffix2 = 'jpg"'
            if peek.endswith(suffix) or peek.endswith(suffix2):
                ln = peek
                logging.info('ln is %s ' % (ln))
                
    except:
        raise Exception("can't find link")
        

    try:
        for j in range(len(dsoup)):
            #find picture name
            logging.debug('The contents of soup are: %s' % (dsoup))
            logging.debug('soup index %s: ' % (dsoup[j]))
            look = dsoup[j]
            suffix = 'alt="'
            if look.startswith(suffix):
                pn = look
                logging.info('ln is %s ' % (ln))
            else:
                logging.info('Couldn\'t find file name starting in:  %s' % (suffix))
                continue
        
    except:
        logging.info('Couldn\'t find file name from link.')        
            
    
    netpic = pn[4:]
    picName = netpic
    rlink = ln
    pic = picName.replace('"', '')
    logging.debug('picName is: %s' % (pic))
    logging.debug('rlink is: %s: ' % (rlink))

    regExUrl2Filename = re.compile(r'("([^"]*)")')
    findLink = regExUrl2Filename.findall(rlink)
    logging.debug('FindLink is: %s' % str((findLink)))
    
    for i in findLink:
        newList = list(i)
        
    logging.debug('NEW LIST HERE : %s' % newList[1])
    xurl = newList[1]
    
    if not xurl.startswith("//imgs.xkcd.com"):
        xurl = "//imgs.xkcd.com/comics/mercator_projection.png"
        
    url = 'https:' + xurl
    logging.debug('PIC: %s : URL: %s' % (pic, url))
    return pic, url
        

#----------------------------------------------------------------------
def downLoadPic(pic, url):
    """Download pic to hdd"""
    
    regexFileName = re.compile(r'((?=\w+\.\w{3,4}$).+)')
    xfileName = regexFileName.search(url)
    fileName = xfileName.group()
    logging.debug('FileName: %s' % (fileName))
    
    
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(fileName, 'wb') as f:
            logging.info('Currently Downloading... %s' % (fileName))
            for chunk in r:
                f.write(chunk)
            f.close()
                
    logDownLoadList = open(swapFile, mode="a+")
    logDownLoadList.write(pic + '\t' + url + '\n')
    logDownLoadList.close()
    
    pwd = os.getcwd()
    logging.debug('Present Directory... %s' % (pwd))
    
    if os.path.exists(fileName):
        logging.info('FileFound %s' % (fileName))
        return True
    else:
        logging.info('File Not Found;  No file downloaded from the site.')
        return False
        
        
        
#----------------------------------------------------------------------
def grabPrevURL(url):
    """Grab the Next URL"""

    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    prevURL = str(soup.select("ul.comicNav"))

    logging.debug('prevURL: %s' % (prevURL))
    
    aTags = soup.find_all(re.compile("^a"))
    bTags = aTags[7]
    
    logging.debug('bTags: %s' % (bTags))
    xbx = str(bTags)
    
    logging.debug('xbx: %s' % (xbx))
    
    regexPreUrl = re.compile(r'(\/\d{1,8}\/)')
    xPreUrl = regexPreUrl.search(xbx)
    
    logging.debug('xPreUrl: %s' % (xPreUrl))
    
    preUrl = xPreUrl.group()  
    logging.debug('preUrl: %s' % (preUrl))
    
    logging.debug('https://xkcd.com%s' % (preUrl))
    return 'https://xkcd.com' + preUrl



#snapPage('https://xkcd.com/2080')
#downLoadPic("firstPic", "http://imgs.xkcd.com/comics/circuit_diagram.png")
#grabPrevURL(mainUrl)
if __name__ == '__main__':
    main()
    logging.debug('Start of Program')
    pic, url = snapPage(mainUrl)
    logging.debug('PIC: %s -- URL: %s' % (pic, url))
    cont = downLoadPic(pic, url)
    nextUrl = grabPrevURL(mainUrl)
    
        
    while cont == True:
        logging.debug('grabing set nextUrl: %s' % (nextUrl))
        pic, url = snapPage(nextUrl)
        logging.debug('grabbed PIC: %s -from- URL: %s' % (pic, url))
        cont = downLoadPic(pic, url)
        logging.debug('bool value of cont: %s' % (cont))
        nextUrl = grabPrevURL(nextUrl)
        logging.debug('setting nextUrl: %s' % (nextUrl))
        print('LOOP')
        
    logging.debug('End of Program')


        
        
    
    
