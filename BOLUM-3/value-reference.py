#value types bellkte değer olarak saklanırlar.
# x=10
# y=20
# x=y
# y=30
# print(x,y)

#Reference types adres olarak bellek üzerinde saklanırlar.
a=["elma","armut"]
b=["elma","armut"]

a=b #b nin adresi ile a nın adresini eşitler.

a[0]="üzüm"

print(a,b)

#Liste Kopyalama Belleğin farklı adreslerinde tutulur.
listeA=[10,20]
#isteB=listeA.copy()
listeB=list(listeA)
listeB[0]=30

print(listeA,listeB)