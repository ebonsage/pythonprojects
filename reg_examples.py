#! python3
#coreyjones

import pprint, re

def isPhoneNumber(text):  # 415-555-0000
    if len(text) != 12:
        return False  #not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
        return False  #missing dash
    if i in range(4, 7):
        if not text[i].isdecimal():
            return False  # no first 3 digets
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  #missing last 4 digets
    return True


pprint.pprint(isPhoneNumber('415-888-6548'))


message = 'Call me 415-555-5896 tomorrow, or at \
    415-585-9865 at my office line'

foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        pprint.pprint('Phone number is found: ' + chunk)
        foundNumber = True
if not foundNumber:
    pprint.pprint('Could not find any phone numbers.')


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo = phoneNumRegex.search(message)
mo2 = phoneNumRegex.findall(message)
pprint.pprint(mo.group())
pprint.pprint(mo2)


###################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")
message2 = 'Call me (415)555-5896 tomorrow, or at \
    (415)585-9865 at my office line'


phoneNumReg = re.compile(r'\((\d\d\d)\)(\d\d\d\-\d\d\d\d)')
momo = phoneNumReg.search(message2)
momo2 = phoneNumReg.findall(message2)
pprint.pprint(momo)
pprint.pprint(momo.group())
pprint.pprint(momo.group(1))
pprint.pprint(momo.group(2))
pprint.pprint(momo2)


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
momomo = batRegex.search('Batman lost the Batmobile and crashed into the Batcopter')
momomo2 = batRegex.findall('Batman lost the Batmobile and crashed into the Batcopter')
pprint.pprint(momomo.group())
pprint.pprint(momomo2)


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

message3 = "The Adventures of Superman and Superwoman"
# ? match the preceding group 1 or more times
superRegex = re.compile(r'Super(wo)?man')
so = superRegex.search(message3)
pprint.pprint(so.group())

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

phoneNumReggie = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')

to = phoneNumReggie.search('My phone number is 415-555-1234 \
                      or Call me tomorrow at 660-2434')

pprint.pprint(to.group())

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

message4 = 'Call me 415-555-5896 tomorrow, or at \
    415 585-9865 at my office line'

phoneRegx = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

tand = phoneRegx.search(message4)

pprint.pprint(tand)


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

message3 = "The Adventures of Superwowowowowowowoman and Superman"
# * match the preceding group 0 or more times
superRegex = re.compile(r'Super(wo)*man')
so = superRegex.search(message3)
pprint.pprint(so.group())


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

message3 = "The Adventures of Superman and Superwoman"
# ?  match the preceding group 0 or 1 more times
# +  match the preceding group 1 or more times
superRegex = re.compile(r'Super(wo)+man')
so = superRegex.search(message3)
pprint.pprint(so.group())


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

message5 = "He said 'HaHaHa'"
message6 = ""

haRegex = re.compile(r'(Ha){3}')
# or haRegex = re.compile(r'(Ha){3,5}') for a range of repetitions
# or haRegex = re.compile(r'(Ha){,5}') for a range of repetitions
# or haRegex = re.compile(r'(Ha){3,}') for a range of repetitions
tator = haRegex.search(message5)
pprint.pprint(tator) 

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

digitRegex = re.compile(r'(\d){3,5}') #greedy match
print(digitRegex.search('1234567890'))

digitRegex = re.compile(r'(\d){3,5}?') #non-greedy match with ? not next to grouping ()
print(digitRegex.search('1234567890'))


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")


message7 = 'Call me 415-555-5896 tomorrow, or at \
    415-585-9865 at my office line, you may reach \
    my wife at 555-439-3894, and sometimes my boat \
    phone at 343-443-5959, table phone number is \
    (404)434-4994'

pprint.pprint(message7)

phoneRegex = re.compile(r'((\()*(\d\d\d)(\))*(-)*(\d\d\d\-\d\d\d\d))')
cook = phoneRegex.findall(message7)
pprint.pprint(cook)


for i in cook:
    #i += 1
    pprint.pprint('This is ' + str(i))
    

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

lyrics = """On the twelfth day of Christmas my true love sent to me: \
12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, \
9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, \
6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, \
2 Turtle Doves, and 1 Partridge in a Pear Tree"""

pprint.pprint(lyrics)

xmaxRegex = re.compile(r'\d+\s\w+')
pepe = xmaxRegex.findall(lyrics)
pprint.pprint(pepe)



########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

#create your own

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')  # r'(a|e|i|o|u) {2} means 2 vowels in a row
poop = vowelRegex.findall(lyrics)
pprint.pprint(poop)

vowelRegex = re.compile(r'[^aeiouAEIOU]{2}')  # ^ means all but whats in []
poop = vowelRegex.findall(lyrics)
pprint.pprint(poop)

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

medtt = "Hello there!"
medtt2 = "He said, 'Hello!"

beginsWithHelloRegex = re.compile(r'^Hello')  # ^ begin and find at the very start of the string.
terr = beginsWithHelloRegex.search(medtt)
terr2 = beginsWithHelloRegex.search(medtt2)
print(terr)
print(terr2)


########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

temem = "On top of the world!"

endsWithWorldRegex = re.compile(r'world!$') # $ means find at end of string 

peope = endsWithWorldRegex.search(temem)
print(temem)

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")


sldkl = '980438903490835'

allDigitsRegex = re.compile(r'^\d+$')
meoe = allDigitsRegex.search(sldkl)
print(meoe)

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

emeo = 'The cat in the hat sat on the flat mat'
emeo2 = 'First Name: Al Last Name: Sweigart'

atRegex = re.compile(r'.at')  #find anything with single char with (at) at the end of the string.
creepo = atRegex.findall(emeo)
print(creepo)


atRegex2 = re.compile(r'.{1,2}at')  #find anything with one or two char that ends with (at).
creepo2 = atRegex2.findall(emeo)    #including spaces
print(creepo2)

atRegex3 = re.compile(r'First Name: (.*) Last Name: (.*)')  # the . is a wildcard that matches anything expect \n new lines
creepo3 = atRegex3.findall(emeo2)
print(creepo3)


# non-greedy .*?   

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
ng = nongreedy.findall(serve)
print(ng)


prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)

primal = re.compile(r'.*', re.DOTALL)  #means everything including \n
app = primal.search(prime)
print(app)


fourlyrics = 'Al, why does your programming book talk about RObOCop so much Asshole?'

vowelRegex2 = re.compile(r'[aeiou]', re.IGNORECASE) #or re.I
memep = vowelRegex2.findall(fourlyrics)
print(memep)

########################################################
#pprint.pprint("THIS IS A NEW INSTANCE BELOW")

#FIND AND REPLACE METHODS
chame = 'Agent Alice gave the secret documents to Agent Bob'

namesRegex = re.compile(r'Agent \w+')
eat = namesRegex.findall(chame)
print(eat)

drink = namesRegex.sub('REDACTED', chame)
print(drink)




########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

namesRegex2 = re.compile(r'Agent (\w)\w*')
eat2 = namesRegex2.findall(chame)
print(eat2)
drink2 = namesRegex2.sub(r'Agent \1*****', chame)
print(drink2)

########################################################
pprint.pprint("THIS IS A NEW INSTANCE BELOW")

re.compile(r'''
(\d\d\d)        # Area Code
-               # first dash
(\(\d\d\d\) )   # first three digits
-               # second dash
\d\d\d\d        # last four digits
\sx\d{2,4} #extension''', re.VERBOSE | re.IGNORECASE | re.DOTALL) 



