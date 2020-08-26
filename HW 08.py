"""
Gabriel Meran
CS 100 2016F Section 021
HW 08 Oct 15,2016
"""

import string
#Problem 1


def fcopy(original,copy):
    fileIn = open(original)
    content = infile.read()
    fileIn.close()
    print(content)

fcopy('example.txt','output.txt')
open('output.txt').read()
'The 3 lines in this file end with the new character.\n\n There is a blank line above this line. \n'

#Problem 2
def stats(fileName):
    infile = open(filename,'r')
    content = infile.read()
    infile.close()
    num_lines = len(content.split('\n'))
    num_words = len(content.split())
    num_chars = len(content.replace('\n',' '))
    print('line count:' + str(num_lines))
    print('word count:' + str(num_words))
    print('character count:' + str(num_chars))

stats('example.txt')

#Problem 3
def repeatWords(Infile,Outfile):
    inF = open(Infile, 'r')
    outF = open(Outfile, 'r+')
    repWords = []
    count = 0
    for lines in inF:
        wordlist = line.lower().split()
    for words in wordlist:
        if(wordList.count(words) > 1 and words not in repWords):
            repWords.append(words)
    for pun in string.punctuation:
        for the_words in repWords:
            if pun in the_words:
                the_words = the_words.replace(pun,'')
                repWords[count] = the_words
                count += 1
            else:
                repWords[count] = the_words
                count += 1
    outF.write(repWords[0])
    outF.write(" ")
    outF.write(repWords[1])
    outF.write("\n")
    outF.write(repWords[2])
print(repeatWords('catInTheHat.txt','catRepWords.txt'))
    
    
