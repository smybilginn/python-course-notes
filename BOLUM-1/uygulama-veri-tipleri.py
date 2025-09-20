"""
# Uygulama1: Yarıçapı verilen dairenin alan ve çevresini bulunuz.
# Alan: pi.r.r
# Çevre:2.pi.r

 yaricap=int(input("Yarıçap giriniz: "))
pi=3

alan=pi*yaricap*yaricap
cevre=2*pi*yaricap

print("Alan = "+str(alan))
print("Çevre = "+str(cevre)) """

#----------------------------------------------------------

"""
Uygulama2: Klavyeden girilen km bilgisini mil cinsinden hesaplayın
mil=km/1.609344

"""
kM=float(input("Km bilgisi giriniz: "))

mil=kM/1.609344

mil=round(mil,2) #virgülden sonra 2 basamak olarak yuvarlar.

print(str(kM)+" km"+" = "+str(mil)+" mil ")