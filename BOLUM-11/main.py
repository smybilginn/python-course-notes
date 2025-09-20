import module

sonuc=module.sayi
sonuc=module.sayilar
sonuc=module.urun
sonuc=module.urun["urunAdi"]
sonuc=module.toplama(5,10)


import module as m

sonuc=m.sayi

from module import sayi,sayilar,urun

sonuc=sayi
sonuc=sayilar
sonuc=urun

from module import*
sonuc=urun
sonuc=toplama(10,5)

print(sonuc)