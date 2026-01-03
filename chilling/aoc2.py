with open('./aoc2_input.txt', 'r', encoding='utf-8') as ff:
    lines = ff.readlines()

total = 0
for num in lines:
    alist = num.split('x')
    alist = [int(x) for x in alist]
    l,w,h = alist
    smallest = min(l*w,w*h, h*l)
    total += (2*l*w + 2*w*h + 2*h*l + smallest)


print(total)