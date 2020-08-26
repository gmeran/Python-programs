def makeWordList(readFileName,writeFileName):
    inF = open(readFileName,'r')
    outF = open(writeFileName ,'w')
    d={}
    for line in inF:
        wordlist = line.split()
        for word in wordlist:
            d[word] = wordlist.count(word)
        for word in d:
            outF.write(word + ' ' + str(d[word]))
            outF.write('\n')
        
    inF.close()
    outF.close()

makeWordList('inputFile.txt','outFile.txt')
        
