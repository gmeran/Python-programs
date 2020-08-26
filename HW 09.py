"""
Gabriel Meran
CS 100 2016F Section 021
HW 09 Oct 18,2016
"""
'MIDTERM 2 2015S'

# Ouestion 1
x=2
for i in range(3):
    print(x,end = ' ')
    x += i
        
'Answer C: 2 2 3'

#Question 2
noise = 'hullaballoo'
idx = 0
while idx < len(noise):
    let = noise[idx]
    print(let, end='')
    letCount = noise.count(let)
    if idx > 2:
        idx += letCount
    else:
        idx += 1
'Answer C: hulll'

#Question 3
s = 'GimmeASlice'
print(2*s[:5] + s[:])

'Answer A : GimmeGimmeGimmeASlice'

#Question 4
noise = 'hullaballoo'
changeCount = 0
for i in range(1, len(noise)):
    if noise[i] != noise[i-1]:
        changeCount += 1
print(changeCount)

'Answer D: 7'

#Question 5
braveOnes = ['Merida', 'Elinor', 'Macintosh', 'Fergus']
vowels = 'aeiou'
for character in braveOnes:
    for vowel in vowels:
        if vowel in character:
            continue
        else:
            print(character[0], end='')
            break
'Answer D: MEMF'

#Question 6
pandemics = [['HIV'], '', ['Ebola', 'SARS'], ['polio', 'smallpox']]
print(pandemics[1:3])

'Answer E: None of the above'

#Question 7
def dictTest(thing, aDict):
    if thing in aDict:
        return thing
    else:
        for v in aDict.values():
            if thing in v:
                return v
types = {'hero':['Alice', 'superman'],'sidekick':['rabbit', 'Jimmy']}
print(dictTest('Alice', types))
'Answer D : [Alice, superman]'

#Question 8
boolExprs = [True and False, not True, True or False, True and not False]
fCount = 0
for expr in boolExprs:
    if expr == False:
        fCount += 1
    else:
        break
print(fCount)
'Answer C: 2'

#Question 9
abe = 'no man has a good enough memory to be a successful liar'
def wordLens(t, limit):
    rtn = []
    aList = t.split()
    for s in aList:
        if len(s) > limit:
            return rtn
        rtn.append(len(s))
    return rtn
print(wordLens(abe, 5))
'Amswer E : None of the above'

#Question 10
def fileCount(fileName, s):
    inF = open(fileName)
    count = 0
    for line in inF:
        count += line.lower().count(s)
    inF.close()
    return count
w = open('seuss.txt', 'w')
w.write('You have brains in your head' + '\n')
w.write('You have feed in your shoes' + '\n')
w.close()
print(fileCount('seuss.txt', 'you'))
'Answer B: 4'

'MIDTERM 2 2015F'

#Question 1
var = 0
num = 1
for i in range(3):
    if i%2 == 0:
        num *= -1
    var += num
    print(var, end = ' ')
'Answer A : -1 -2 -1'

#Question 2
scary = 'boo! boo!'
place = 0
while place <= len(scary):
    current = scary[place]
    print(current, end='')
    place += scary.count(current)
'Answer B: boo'

#Question 3
eap = 'rapping, rapping'
print(eap[:4] + eap[-4:])
'Answer B: rappping'

#Question 4
seasonal = 'boo'
out = ''
idx = 0
while True:
    letter = seasonal[idx]
    letterCount = seasonal.count(letter)
    out += letter
    if seasonal[idx] > seasonal[idx+1]:
        idx += letterCount
    elif seasonal[idx] < seasonal[idx+1]:
        idx -= letterCount
    else:
        break
print(out)
'Answer D: boo'

#Question 5
favs = ['Leia', 'R2-D2', 'Solo', 'Chewbacca']
vowels = 'aeiou'
for vowel in vowels:
    for fav in favs:
        if vowel in fav:
            continue
        else:
            print(fav[0], end='')
            break
'Answer D: RRRLL'

#Question 6
pairs = {'':'empty', 2:'prime', 1:['polio', 'smallpox']}
print(pairs[1][1])
'Answer E: none of the above'

#Question 7
def dictTest(aType, aDict):
    if aType in aDict:
        return aType
    else:
        for v in aDict.values():
            if aType in v:
                return v
types = {string:'string', num:0, tuple:('a','ok')}
print(dictTest('string', types))
'Answer D: NameError: name string is not defined'

#Question 8
boolExprs = [True and False, not True, True or False, True and not False]
tCount = 0
for expr in boolExprs:
    if expr == True:
        tCount = 2*tCount + 1
    else:
        break
print(tCount)
'Amswer E: none of the above'

#Question 9
def contains(txt, letters):
    rtn = []
    aList = txt.split()
    for w in aList:
        if w in letters:
            rtn.append(w)
    return rtn
burns = "a man's a man for a' that"
print(contains(burns, 'abc'))
'Answer B: [a , a]'

#Question 10
def fileCount(fileName, s):
    inF = open(fileName)
    count = 0
    content = inF.read()
    for thing in content:
        if s in thing:
            count += 1
    inF.close()
    return count
w = open('seuss.txt', 'w')
w.write('You are on your own' + '\n')
w.write('and you know what you know' + '\n')
w.close()
print(fileCount('seuss.txt', 'you'))
'Answer E: nome of the above'
