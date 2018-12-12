#!/usr/bin/env python
#coding:utf-8
"""
  Author:  coreyjones --<>
  Purpose: 
  Created: 12/12/2018
"""

import os, sys, pafy, logging

url = "https://www.youtube.com/watch?v=SLsTskih7_I"
dlcheck = False  #dlcheck - Set to "True" to download - Set to "False for dryrun"
video = pafy.new(url)
downloadFolder = 'C:\\youtube_videoDownlods'
loggingFile = '%s\\Program_Log' % (downloadFolder)
vidTitle = video.title
vidRating = video.rating
vidViews = video.viewcount
vidAuthor = video.author
vidLength = video.length
vidDuration = video.duration
vidLikes = video.likes
vidDislikes = video.dislikes
vidDesc = video.description


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

os.chdir(downloadFolder)
pwd = os.getcwd()
logging.info('PWD:  %s' % (pwd))

streams = video.streams



for s in streams:
    print(s)
    print(s.resolution, s.extension, s.get_filesize(), s.url)
    
allstreams = video.allstreams
for s in allstreams:
    print(s.mediatype, s.extension, s.quality)
    

best = video.getbest()
bestPref = video.getbest(preftype='webm') #mv4,webm,flv,3gp 

#get url, for download of streaming in vlc
#print('BEST URL')
#print(best.url)
#print('BEST PREF URL')
#print(bestPref.url)

filename_path = "%s\\%s." % (downloadFolder, vidTitle)


if not os.path.exists(filename_path):
    logging.info('File to Download:  %s' % (filename_path))
    if dlcheck == True:
        filename = best.download(filepath=filename_path + best.extension)
    print("Best video file available to download is: %s and has finished downloading." % (best))



#audiostreams = video.audiostreams
#for a in audiostreams:
    #print(a.bitrate, a.extension, a.get_filesize())



audioHelp = """   

256k m4a 331379079
192k ogg 172524223
128k m4a 166863001
128k ogg 108981120
48k m4a 62700449

Downlad the 2nd audio stream from above list.

audiostreams[1].download()

"""

#bestAudio = video.getbestaudio()
#bestAudioPref = video.getbestaudio(preftype="m4a")
#bestBitRate = bestAudio.bitrate

#print(bestAudio)
#print(bestBitRate)



























#if __name__ == '__main__':
    #unittest.main()