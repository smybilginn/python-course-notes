a,b,c=4,8,(12,2)

"""
#1-Kullanıcıdan aldığınız iki sayının çarpımı ile a,b,c toplamının farkı nedir?
sayi1=int(input("1. sayı:"))
sayi2=int(input("2. sayı:"))

carpim=sayi*sayi2

toplam=a+b+c[0]+c[1]
print("Toplam "+ str(toplam))

fark=carpim-toplam

print(fark)

#----------------------------------------------------------------------------
#2-c'nin b'ye kalansız bölümünü hesaplayınız
sonuc=(c[0]+c[1])//b
print(sonuc)

#----------------------------------------------------------------------------
#3-a,b,c toplamının mod 7 si nedir?
cToplam=c[0]+c[1]

toplam=a+b+cToplam

mod=toplam%7

print(mod)

#---------------------------------------------------------------------------
#4-b'nin a. kuvvetini hesaplayınız.
b**=a
print(b)

#---------------------------------------------------------------------------
#5-a,*b,c=(2,4,6,8,13) işlemine göre c'nin küpü nedir?
a,*b,c=(2,4,6,8,13) #a:2 c:13 ü alır. Aradaki değerleri ise b alır.
print(c**3)

#----------------------------------------------------------------------------
#6- a,b,*c=(2,4,6,8,13) işlemine göre c'nin değerleri toplamı nedir?
a,b,*c=(2,4,6,8,13)

print(c[0]+c[1]+c[2])

"""