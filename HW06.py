"""
Gabriel Meran
CS 100 2016F Section 021
HW 06 Oct 8,2016
"""

'''
Problem 1
'''
def twoWords(length,firstLetter):
    while True:
        emplist = []
        numletter = str.length
        letter = input( numletter + 'letter word please')
        word = input('A word beginning with' + firstLetter + 'please')
        if (len(letter) == length):
            emplist.append(letter)
        if(firstLetter == word[0]):
            emplist.append(word)
            break
        return emplist
print(twoWords(4,'B')

'''
Problem 2
'''
def twoWords(length,firstLetter):
    while True:
        emplist = []
        numletter = str.length
        letter = input( numletter + 'letter word please')
        word = input('A word beginning with' + firstLetter + 'please')
        if (len(letter) == length):
            emplist.append(letter)
      continue
        if(firstLetter == word[0]):
            emplist.append(word)
      return emplist
print(twoWords(4,'B')

'''
Problem 3
'''
def lastfirst(name):
    first = []
    last = []
    return last[] + ',' + first[]


'''
problem 4
'''
def mystery(n):
    count = 0
    while n > 1:
        n = n /2
        count += 1
    if n ==1
    return count 
'''
Problem 5
'''
def enterNewPassword():
    password = input('enter your password')
    while len(password) >= 8 and len(password) <= 15:
        print('password accepted')
        break      
