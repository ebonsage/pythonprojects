#! python3
import re, pyperclip, sys, pprint

#campus directory filetype:pdf
#TODO: Create a regex for phone numbers and emails, etc.
phoneRegex = re.compile(r'''
# 555-555-5555, (555) 555-5555
# +55-5-5555555, +55-5-555-, +5555555-5555, +55-55-5555-, +55555555555, +55 555 555 55, +55 5 5555
(
\(?(\d\d\d)\)?         # ((\d\d\d)|(\(\d\d\d\)))? area code (optional)
[ -]?                          # (\s|-) first separator
(\d\d\d)                          # \d\d\d first 3 digits
[ -]?                              # - separator
(\d\d\d\d)                         # \d\d\d\d last 4 digits
 
)
''', re.VERBOSE)

extNumRegEx = re.compile(r'(((ext(\.)?\s)|x)(\d{2,5}))')

phToExtRegEx = re.compile(r'''
(
(((ext(\.)?\s)|x)(\d{2,5}))?
\s
\(?(\d\d\d)\)?         # ((\d\d\d)|(\(\d\d\d\)))? area code (optional)
[ -]?                          # (\s|-) first separator
(\d\d\d)                          # \d\d\d first 3 digits
[ -]?                              # - separator
(\d\d\d\d)                         # \d\d\d\d last 4 digits
)
''', re.VERBOSE)


#TODO: Create a regex for email addresses
emailRegex = re.compile(r'([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})')

#TODO: Get the text off the clipboard
text = pyperclip.paste()
#print(text)
#TODO: Extract the email/phone from the text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
extractedExtensions = extNumRegEx.findall(text)
extractedP2E = phToExtRegEx.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

allExtensionPh = []
for extPhoneNumber in extractedExtensions:
    allExtensionPh.append(extPhoneNumber[0])
    
allext2PhNumber = []
for ext2phon in extractedP2E:
    allext2PhNumber.append(ext2phon[0])

pprint.pprint(allPhoneNumbers)
pprint.pprint(extractedEmail)
pprint.pprint(allExtensionPh)
pprint.pprint(allext2PhNumber)
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail) + '\n' \
    + '\n'.join(allext2PhNumber)


pyperclip.copy(results)