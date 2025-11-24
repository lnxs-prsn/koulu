sentence = 'hello this is sentence'
char = ' '
def my_slice(sentence, char):
    blist = []
    element = ''
    for x in range(sentence.count(char)):
        if x == ' ':
            blist.append(element)
            element = ''
        elif x == sentence[-1]:
            element += x
            