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
ferfi = 0
no = 0
db = 0
f = open('UTONEV.TXT', 'rt' , encoding = 'ansi')
f.readline()

for sor in f :
    tmp = sor.strip().split(';')
    utonevek.append(Nev(tmp[0], tmp[1], tmp[2], tmp[3],tmp[4], tmp[5]))
    db += 1
for utonev in utonevek:
    print(utonev)

ffo = 0
for ferfi in utonevek:
    if ferfi.nem == 'F':
        if ferfi.elso != '':
            ffo += int(ferfi.elso)
print(f"{ffo} férfi volt")

nfo = 0
for no in utonevek:
    if no.nem == 'N':
        if no.elso != '':
            nfo += int(no.elso)
print(f"{nfo} nő volt")

print(f"{ffo + nfo} volt a népesség száma")

print(f"{db} utónévről van adat")