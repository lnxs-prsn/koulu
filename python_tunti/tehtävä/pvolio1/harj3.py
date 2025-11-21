# class Studen():
#     def __init__(self, etunimi, sukunimi):
#         self.etunimi = etunimi
#         self.sukunimi = sukunimi
#     alist = []
#     def suorkurssi(self, kurssi):
#         self.kurssi = kurssi
#         self.alist.append(kurssi)

#         return f'{kurssi} lisätty suoritettuihin'
    
#     def printkurssi(self):
#         if self.alist:
#             for x in self.alist:
#                 print(x)
#         else:
#             print(f'{self.etunimi} {self.sukunimi} has not completed any course')

# stde = Studen('Said', 'Ahmed')
# # stde.suorkurssi('python')
# # stde.suorkurssi('javascript')
# stde.printkurssi()



class Studen():
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.alist = []
   
    def suorkurssi(self, *args):
        for x in args:
            self.alist.append(x)

        return f'{x} lisätty suoritettuihin'


    def printkurssi(self):
        if self.alist:
            for x in self.alist:
                print(x)
        else:
            print(f'{self.etunimi} {self.sukunimi} has not completed any course')

stde = Studen('Said', 'Ahmed')
stde.suorkurssi('python','javascript')
stde.printkurssi

