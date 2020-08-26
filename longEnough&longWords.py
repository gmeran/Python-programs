def longEnough(s,threshold):
    if len(s) == threshold:
        return True
    else:
        return False
print(longEnough('Amen',4))

def longWords(t,i):
    d={}
    wordlist = t.split()
    for word in wordlist:
        longEnough(word,i)
        if word in d:
            d[word] += 1
        else:
            d[word] =1
    if longEnough(word,i) == True:
        return d
            
text='one fish two fish red fish blue fish'
print(longWords(text,4))
