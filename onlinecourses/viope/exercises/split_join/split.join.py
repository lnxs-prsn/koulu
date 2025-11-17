sentence = 'hello this is sentence'
char = ' '
def my_split(sentence, char):
    alist = []
    val = 0
    while ' ' in sentence:
        alist.append(sentence[val: sentence.find(' ')])
        val = sentence.find(' ') +1
    return alist
print(my_split(sentence, ' '))


def my_joind(alist, char):
    pass