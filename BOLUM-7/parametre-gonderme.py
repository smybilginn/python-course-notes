def selamlama(isim):
    return "Merhaba, "+isim

#print(selamlama("Sümeyye"))

def yasHesapla(dogumYili):
    return 2025-dogumYili

#print(yasHesapla(1998))

def emekliligeKacYilKaldi(dogumYili,isim):
    yas=yasHesapla(dogumYili)

    kalanSure=65- yas

    if kalanSure>0:
        return f"{isim} emekliliğine {kalanSure} yıl kaldı."
    else:
        return f"{isim} zaten {abs(kalanSure)} yıl önce emekli oldun."
    
print(emekliligeKacYilKaldi(1998,"Sümeyye"))
print(emekliligeKacYilKaldi(1950,"Ayşe"))

def toplam(sayi1,sayi2):
    return sayi1+sayi2

#print(toplam(10,30))