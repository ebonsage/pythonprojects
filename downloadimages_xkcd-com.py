#!/usr/bin/env python
#coding:utf-8
#coreyjones

"""
  Author: coreyjones  --<>
  Purpose: Download all pictures from https://xkcd.com and log each download
  Created: 12/10/2018
"""
import os, sys, requests, bs4, re, pprint

mainUrl = 'https://xkcd.com'
downloadFolder = 'C:\\picbot'
swapFile = '%s\\pic_names.txt' % (downloadFolder)
#url = ''
#pic = ''

#----------------------------------------------------------------------
def main():
    """"""
    if not os.path.exists(downloadFolder):
        os.makedirs(downloadFolder)
    
    assert os.path.isdir(downloadFolder), 'Download folder is missing! ' + str(downloadFolder)
    
    os.chdir(downloadFolder)
    pwd = os.getcwd()   
    #pprint.pprint(pwd)
    
    if not os.path.exists(swapFile):
        swap = open(swapFile, mode='w+')
        swap.write('BEGIN DOWNLOAD LOG' + '\n\n\n\n')
        swap.close()
        
#----------------------------------------------------------------------
def snapPage(url):
    """Pull current page"""
    
    res = requests.get(url)
    res.raise_for_status()         

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    csoup = str(soup.select("[id~=comic]"))
    pprint.pprint(csoup)
    
    dsoup = csoup.split(" ") #create a list
    
    try:
        for i in range(len(dsoup)):
            #find link
            print(i)
            print(dsoup[i])
            peek = dsoup[i]
            suffix = 'png"'
            if peek.endswith(suffix):
                ln = peek
                print(ln)
            else:
                continue
        
    except:
        raise Exception("can't find link")
        

    try:
        for j in range(len(dsoup)):
            #find picture name
            #print(j)
            #print(dsoup[j])
            look = dsoup[j]
            suffix = 'alt="'
            if look.startswith(suffix):
                pn = look
                print(pn)
            else:
                continue
        
    except:
        raise Exception("can't find name")        
            

    
    picName = pn
    rlink = ln
    pic = picName.replace('"', '')
    print("picName is: " + pic)
    print("rlink is: " + rlink)

    regExUrl2Filename = re.compile(r'("([^"]*)")')
    findLink = regExUrl2Filename.findall(rlink)
    print("This FIndLink " + str(findLink))
    
    for i in findLink:
        newList = list(i)

    print("NEW LIST HERE " + newList[1])
    xurl = newList[1]
    
    url = 'https:' + xurl
    print(pic, url)
    return pic, url
        

#----------------------------------------------------------------------
def downLoadPic(pic, url):
    """Download pic to hdd"""
    
    regexFileName = re.compile(r'((?=\w+\.\w{3,4}$).+)')
    xfileName = regexFileName.search(url)
    fileName = xfileName.group()
    
    pprint.pprint(fileName)
    
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(fileName, 'wb') as f:
            pprint.pprint('Downloading... '+ fileName)
            for chunk in r:
                f.write(chunk)
            f.close()
                
    logDownLoadList = open(swapFile, mode="a+")
    logDownLoadList.write(pic + '\t' + url + '\n')
    logDownLoadList.close()
    pwd = os.getcwd()
    pprint.pprint(pwd)
    if os.path.exists(fileName):
        return True
    else:
        return False
        
        
        
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
    
    #pprint.pprint(bTags)
    #pprint.pprint(type(bTags))
    
    xbx = str(bTags)
    
    #pprint.pprint(xbx)
    
    regexPreUrl = re.compile(r'(\/\d{1,8}\/)')
    xPreUrl = regexPreUrl.search(xbx)
    
    #print(xPreUrl)
    
    preUrl = xPreUrl.group()    
    pprint.pprint(preUrl)
    
    #print('https://xkcd.com' + preUrl)
    
    return 'https://xkcd.com' + preUrl







    



#snapPage('https://xkcd.com/2080')
#downLoadPic("firstPic", "http://imgs.xkcd.com/comics/circuit_diagram.png")
#grabPrevURL(mainUrl)



if __name__ == '__main__':
    main()
    
    pic, url = snapPage(mainUrl)
    print(pic + ' ' + url)
    cont = downLoadPic(pic, url)
    nextUrl = grabPrevURL(mainUrl)

        
    while cont == True:
        print(nextUrl)
        pic, url = snapPage(nextUrl)
        print(pic + ' ' + url)
        cont = downLoadPic(pic, url)
        print(cont)
        nextUrl = grabPrevURL(nextUrl)
        print(nextUrl)

        
        
    
    
