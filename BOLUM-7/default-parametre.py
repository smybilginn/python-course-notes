def selamlama(isim="Kullanıcı",mesaj="İyi günler"):
    return f"{mesaj} {isim}"

sonuc=selamlama("Sümeyye")
#print(sonuc)

def usAlma(taban,us=2):
    return taban**us

sonuc=usAlma(2,4)
sonuc=usAlma(2)
#print(sonuc)

def toplam(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def islem(a,b,fn=toplam):
    return fn(a,b)

sonuc=islem(5,4,cikarma)
print(sonuc)