title="Python ile Programlama Dersleri"

"""
#1-title değişkeni içerisindeki karakter sayısı nedir?
karakterSayi=len(title)
print(karakterSayi)

"""
"""
#2-tittle içerisindeki python kelimesini alın.
print(title[0:7])

"""

"""
#3-tittle değişkeninin ilk 5 ve son 5 karakterini alın
print("ilk 5: ",title[0:6]," son 5:", title[:-5])
"""
"""
#4-tittle değişkeninin tersten yazdırın.
print(title[::-1])
"""
#5-Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız
#Cümle: Çınar Turan isimli öğrencinin 1. notu 60, 2.noru 60 ve not ortalaması 60 olarak hesaplanmıştır.

ad=input("İsim giriniz: ")
soyad=input("Soyisim giriniz: ")
not1=float(input("1. Sınav notu: "))
not2=float(input("2. Sınav notu: "))
ort=(not1+not2)/2

msj=f"{ad} {soyad} isimli öğrencinin 1. notu {not1}, 2. notu{not2} ve not ortalaması {ort} olarak hesaplanmıştır."

print(msj)
