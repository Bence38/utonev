class Nev:
    def __init__(self, nev,elso,masodik,ujsz1,ujsz2,nem):
        self.nev = nev
        self.elso = elso
        self.masodik = masodik
        self.ujsz1 = ujsz1
        self.ujsz2 = ujsz2
        self.nem = nem



f = open('UTONEV.TXT', 'rt' , encoding = 'ansi')

nevek = []
for sor in f :
    tmp = sor.split()
    nevek.append(tmp)
print(nevek)