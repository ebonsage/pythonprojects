#!/usr/bin/env python
#coding:utf-8
"""
  Author:  coreyjones --<>
  Purpose: 
  Created: 12/12/2018
"""

import os, sys, pprint, pafy, logging

downloadFolder = 'C:\\youtube_videoDownlods'
loggingFile = '%s\\Program_Log' % (downloadFolder)

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

pp = pprint.pprint
url = "https://www.youtube.com/watch?v=uyr7GPMX050"
video = pafy.new(url)

vidTitle = video.title
vidRating = video.rating
vidViews = video.viewcount
vidAuthor = video.author
vidLength = video.length

vidDuration = video.duration
vidLikes = video.likes
vidDislikes = video.dislikes
vidDesc = video.description

pp(vidDesc)
pp(vidLikes)
pp(vidTitle)

streams = video.streams

for s in streams:
    print(s)
    print(s.resolution, s.extension, s.get_filesize(), s.url)


best = video.getbest()
bestPref = video.getbest(preftype='mp4') #mv4,webm,flv,3gp 



#get url, for download of streaming in vlc
pp('BEST URL')
pp(best.url)
pp('BEST PREF URL')
pp(bestPref.url)

filename_path = "%s\\%s." % (downloadFolder, vidTitle)


if not os.path.exists(filename_path):
    logging.info('File to Download:  %s' % (filename_path))
    #filename = best.download(filepath=filename_path + best.extension)


audiostreams = video.audiostreams
for a in audiostreams:
    print(a.bitrate, a.extension, a.get_filesize())



audioHelp = """   

256k m4a 331379079
192k ogg 172524223
128k m4a 166863001
128k ogg 108981120
48k m4a 62700449

Downlad the 2nd audio stream from above list.

audiostreams[1].download()

"""

bestAudio = video.getbestaudio()
bestAudioPref = video.getbestaudio(preftype="m4a")

bestBitRate = bestAudio.bitrate

print(bestAudio)
print(bestBitRate)



























#if __name__ == '__main__':
    #unittest.main()