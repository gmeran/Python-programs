"""
Gabriel Meran
CS100 2016F Section 021
Sept 21,2016
"""


#1
value = 0
if True and False:
 value += 1
elif not True or not False:
 value += 2
else:
 value += 4
if True or False:
 value += 8
elif True:
 value += 16
print(value)
"""
Answer a) 10
"""
#2
aSeq = [-2, -1, 0, 1]
sum = aSeq[-2] + aSeq[0] + aSeq[1]
print(sum)

"""
Answer c) -3
"""
#3
nested = [[''], '', 0]
print(nested[1:2])

"""
Answer d) ['']
"""
#4
aList = [-2, '-1', 0, 1, 2]
leading = aList[:2]
trailing = aList[-3:]
print( leading + trailing)

"""
Answer c) [-2, '-1' , 0, 1, 2]
"""
#5
import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(7):
 if i%2 == 1:
     t.forward(100)
     t.right(90)


"""
Answer b) three sides of a square
"""
#6
def makePalindrome(aStr):
    idx = -1
    image = ""
    for i in aStr:
        image += aStr[idx]
        idx -= 1
    return aStr+image
palindrome = makePalindrome("aha")
print(palindrome)

"""
Answer c) ahaaha
"""
#7
turnWest = False
turnEast = True
if turnWest:
 print('Jersey floods')
if turnEast:
 print('dodged a hurricane')
else:
 print('basements stay dry')

"""
Answer a) dodged a hurricane
"""
#8
hasDescender = 'gjpqy'
star = 'miss piggy'
myStr = ''
for letter in star:
 if letter not in hasDescender:
     myStr += letter
print(myStr)
"""
Answer c) miss i
"""
#9
def compareLength(thing, optLength):
 thingLen = len(thing)
 if optLength-thingLen > 3:
     return 'too short'
 if optLength > thingLen:
     return 'less than opt'
 if thingLen == optLength:
     return 'optimal'
comparison = compareLength('foot', 12)
print(comparison)

"""
Answer a) too short
"""
#12
beatleLine = 'I am the walrus'
def vowelCount(text):
    count = 0
    for i in range text:
        if i in ' aeiouAEIOU':
            count += 1
    return count
print(vowelCount(beatleLine))
#13


def getInitials(remark):
    first = input('Whats your first name?')
    last = input('Whats your last name?')
    print(remark + ' ' + first + ' ' + last)
    return first[0] + last[0]
intials = getInitials('Thank You')
print(intials)



