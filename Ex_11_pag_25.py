n=int(input('Dati numarul de elemente din vector='))
z=[]
# if n<10:
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    z.extend([x])
print(z)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii:',*z[0:5])

print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator:',*z[::-1])
b=sorted(z)
b.sort(reverse=True)
print('c)  sortează componentele tabloului în ordine descrescătoare;')
c=sorted(z)
c.sort(reverse=True)
print(c)

print('d)  afişează pe ecran doar componentele pare;')
d=[]
for i in range(0,len(z)):
    if z[i]%2==0:
        y=z[i]
        d.extend([y])
print(d)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')
import statistics
e=statistics.mean(d)
print(e)
print('f)  afişează pe ecran doar componentele impare;')
f=[]
for i in range(0,len(z)):
    if z[i]%2!=0:
        y=z[i]
        f.extend([y])
print(f)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x,y=eval(input('Introduceti x,y:'))
g=[]
for i in z:
    if(i>x) and (i%y!=0):
        g.extend([i])
        print(g)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
h=[]
for j in z:
    if(j>x) and (j<y):
        h.extend([j])
        print(h)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
i=[]
for v in z:
    if(v<0) and (v%2!=0):
        i.extend([z.index(v)])
        print(i)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
j=[]
for b in z: 
    if ((abs(b) // 10) < 10) and ((abs(b) // 10) > 0):
        j.extend([z.index(b)])
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
z1=z.copy()
z1[0]=min(z)
print(z1)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
z2=z.copy()
z2[z2.index(min(z2))]=z2[0]
print(z2)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
z3=[]
for q in z:
    if (q % 2 == 0):
        z3.extend([q])
        print(z3)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
z4=[]
for w in z:
    if (w % 3 == 0):
        z4.extend([w])
        print(z4)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')
z5=[]
for e in z:
    if len([r for r in range(1, e + 1) if e % r == 0]) <= 4:
        z5.append([e])
        print(z5)