kurum="BTK AKADEMİ".split() #str to list

print(kurum)
print(kurum[0])
print(kurum[1])

print(type(kurum)) #<class 'list'> - liste tipini verir.
print(type(kurum[0])) #<class 'str'> - liste içerisindeki elemanın tipini cerir.

sayilar=[1,2,3,4,5]
isimler=["ahmet","ayşe","fatma"]

ogrenci=["Çınar","Turan",60,50,70]

ortalama=(ogrenci[2]+ogrenci[3]+ogrenci[4])/3

print(ortalama)

#-----------------------------------------------------------------------------------------

ogrenciler=[["Çınar","Turan",50,60,70],["Ali","Turan",80,40,90]]
print(ogrenciler[0][0]) #ogrenciler listesindeki 0. elemanın 0. indexi
print(ogrenciler[1][3]) #ogrenciler listesindeki 1. elemanın 3. indexi

#Pratik Uygulama
ort=((ogrenciler[0][2]+ogrenciler[0][3]+ogrenciler[0][4])/3)

print("Öğrenci "+ ogrenciler[0][0]+" Not ortalaması: "+str(ort))
