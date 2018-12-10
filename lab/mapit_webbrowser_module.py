import webbrowser, sys, pyperclip, pprint
#coreyjones

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed.
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    rawaddress = ' '.join(sys.argv[1:])
else:
    rawaddress = pyperclip.paste()
    
address = rawaddress.replace(',', ' ')

pprint.pprint('https://www.google.com/maps/place/' + address)
webbrowser.open('https://www.google.com/maps/place/' + address)
