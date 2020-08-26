"""
Gabriel Meran
CS100 2016F Section 021
HW 05 Sept 25,2016
"""
#1
snap_freeze = True
blizzard = False
if snap_freeze and blizzard:
    print('1')
elif not snap_freeze or not blizzard:
    print('2')
if snap_freeze or blizzard:
    print('3')
else:
    print('4')

"""
Answer e) none of the above it prints 2 and 3
"""
#2
letters = ['p','y','t','h','o','n']
concat = letters[3] + letters[-2] + letters[2]
print(concat)

"""
Answer b) hot
"""
#3
someStrings = ['cs', '100', 'midterm']
print(someStrings[1:2])

"""
Answer c) ['100']
"""
#4
aList = [2, -1, -2]
sliceA = aList[:2]
sliceB = aList[-1:]
print(sliceA + sliceB)
"""
Answer b) [2,-1,-2]
"""
#5
import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(5):
    if i//4 == 0:
        t.forward(100)
        t.right(90)

"""
Answer c) square
"""
#6
def letterCount(aStr, aLetter):
    if aLetter in aStr:
        return True
    elif aStr.count(aLetter) > 1:
        return 'many'
    return False
result = letterCount("loop", 'o')
print(result)
"""
Answer a) True
"""
#7
electionYear = True
leapYear = True
if electionYear:
    print('lots of ads')
if not leapYear:
    print('Feb has 28')
else:
    print('quadrennial')
"""
Answer c) lots of ads quadrennial
"""
#8
caps = 'ABCDEFGHIJKLMNOPQRSTUVWYXY'
vowels = 'aeiouAEIOU'
etiquette = 'do not SHOUT'
myStr = ''
for letter in etiquette:
    if letter in vowels or letter in caps:
        myStr += letter
print(myStr)
"""
Answer a) ooShout
"""
#9
def compareSize(anObject, length):
    objectLen = len(anObject)
    if objectLen == length:
        return 'equal'
    if objectLen == 0:
        return '0'
    else:
        return 'not 0'
    return objectLen
print(compareSize('week', 7))
"""
Answer b) not 0
"""
#10
def rangeExample(aString, stop, interval):
    returnVal = ''
    myRange = range(1, stop, interval)
    for idx in myRange:
        returnVal += aString[idx]
    return returnVal
print(rangeExample('Do unto others', 13, 4))

"""
Answer e) None of the above
"""

#11a
import turtle
s = turtle.Screen()
t = turtle.Turtle()
def drawSquare(t,length):
    for i in range(4):
        t.foward(length)
        t.left(90)

#13
def getDate(message):
    month=input('what month is it?')
    day=int(input('what day is it?'))
    print(month+' '+ str(day)+ ' '+message)
    return month + ' ' + str(day)
today = getDate('is a great day!')
print(today)

    
    
    
    

