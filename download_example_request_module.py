import os, sys, pprint, requests
#coreyjones

url = 'http://google.com'

os.chdir('c:\\delicious')
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

pprint.pprint(res.status_code)
pprint.pprint(res.headers['content-type'])
pprint.pprint(res.encoding)
#pprint.pprint(res.json)
#pprint.pprint(res.text[:500])


playFile = open('RomeoAndJuliet.txt', mode='wb', buffering=2)
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

headers = {'user-agent': 'themoon/3.4.5'}
r = requests.get(url, headers=headers)
pprint.pprint(r)
pprint.pprint(r.headers)
pprint.pprint(r.cookies['NID'])



