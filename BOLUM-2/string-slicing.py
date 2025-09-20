kurs="Python ile programlama"

adet=len(kurs) #len boşluk dahil kaç karakter old gösterir.
print(adet)

print(kurs[adet-1]) #en son karakteri verir.

print(kurs[0:6]) #0 dan 6 ya kadar olan karakterleri verir. 6 dahil değil.
#print(kurs[:6]) da aynısı

print(kurs[11:len(kurs)]) #print(kurs[11:]) aynısı

print(kurs[0:20:2]) #2 yazdığımız için adımda bir karakter alır birini almaz.

print(kurs[: :-1]) #stringi ters çevirir.