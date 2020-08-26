def mostFrequent(inFile,outFile):
    inF = open(inFile,'r')
    outF = open(outFile,'w')
    d={}
    content = inF.readlines()
    for line in content:
        wordlist = line.split()
        for word in wordlist:
            for char in word:
                if char in d :
                    d[char] += 1
                else:
                    d[char] = 1
        for char in d:
            if d[char]>=3:
                outF.write(char)
        outF.write('\n')
    inF.close()
    outF.close()
mostFrequent('moreYouRead.txt','moreYouReadOut.txt')
                    
