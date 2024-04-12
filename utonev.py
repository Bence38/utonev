class Nev:
    def __init__(self, nev,elso,masodik,ujsz1,ujsz2,nem):
        self.nev = nev
        self.elso = elso
        self.masodik = masodik
        self.ujsz1 = ujsz1
        self.ujsz2 = ujsz2
        self.nem = nem

    def __str__(self):
        return f'Utónév: {self.nev}, Neme: {self.nem}'
utonevek = []
f = open('UTONEV.TXT', 'rt' , encoding = 'ansi')
f.readline()

for sor in f :
    tmp = sor.strip().split(';')
    utonevek.append(Nev(tmp[0], tmp[1], tmp[2], tmp[3],tmp[4], tmp[5]))
for utonev in utonevek:
    print(utonev)