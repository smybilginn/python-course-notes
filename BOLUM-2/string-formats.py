ad="Sadık"
soyad="Turan"
yas=40

"""

#1. BİRLEŞTİRME YÖNTEMİ

msj="My name is "+ad+" "+soyad+" I'm "+str(yas)+" years old."
print(msj)

"""
""" 
#2.BİRLEŞTİRME YÖNTEMİ
msj="My name is {0} {1}. I'm {2} years old.".format(ad,soyad,yas)
print(msj)

veya 

msj="My name is {ad} {soyad}. I'm {yas} years old.".format(ad,soyad,yas)
print(msj)

"""
#3.BİRLEŞTİRME YÖNTEMİ
msj=f"My name is {ad} {soyad}. I'm {yas} years old."
print(msj)

