t = '20x3x11'
summa = 0




with open('input_2015_2.txt', 'r') as file:
    lines = file.readlines()
    for x in lines:
        
        l,w,h = x.split('x')
        l,w,h = int(l),int(w),int(h)
        a1,a2,a3 = (l*w),(w*h),(h*l)
        summa += (( 2*l*w + 2*w*h + 2*h*l)+min([a1,a2,a3]))
        


       

print(summa)