def vowelCount(s):
    vowels = 'AEIOUaeiou'
    vowelcnt = 0
    for char in s:
        if char in vowels:
            vowelcnt += 1
    '''print(vowelcnt)'''
    return vowelcnt
vowelCount('Amendment')

def manyVowels(t,i):
    d = {}
    wordlist = t.split()
    for word in wordlist:
        vowelCount(word)
        if vowelCount(word)>=i:
            d[word] = vowelCount(word)
    return d
  
            
text = 'they are endowed by their creator with certain unalienable rights'''
print(manyVowels(text,3))
