sentence = 'hello this is sentence'
char = ' '
def my_slice(sentence, char):
    blist = []
    element = ''
    for index, x in enumerate(sentence):
        if x == ' ':
            blist.append(element)
            element = ''
        elif index == len(sentence)-1:
            element += x
            blist.append(element)
            element = ''
        else:
            element += x


        
    return blist
    print(blist)
alist = my_slice(sentence, ' ')



def my_join(alist: list, char: str):
    string = ''
    for word in alist:
        if word == alist[-1]:
            string += word
        else:
            string += word+char
    return ''
print(my_join(alist, ','))