def repeatWords(inputF,outputF):
    inF = open(inputF,'r')
    outF = open(outputF,'w')
    d={}
    for line in inF:
        wordlist = line.split()
        for word in wordlist:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        for word in d:
            if d[word]>1:
                outF.write(word + ' ' + str(d[word]))
                outF.write('\n')
    inF.close()
    outF.close()
repeatWords('example2.txt','example2out.txt')
