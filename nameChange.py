''' define functiom called nameChange that accept 2 parameter:
string name, int increment and returns a string wih every
'increment' letter of the name
'''
def nameChange(name,increment):
    tmp = ' '
    for i in range(0,len(name),increment):
        tmp += name[i]
    return(tmp)
print(nameChange('vincent',3))
