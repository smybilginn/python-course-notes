#1-"Toyota","BMW","RENAULD","MERCEDES" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar=["TOYOTA","BMW","RENAULD","MERCEDES"]
"""
#2-Liste kaç elemanlıdır?
print(len(markalar))

#3-Listenin ilk ve son elemanı nedir?
print("Listenin ilk elemanı:",markalar[0]+" listenin son elemanı:"+markalar[-1])

#4-RENAULD markasını TOGG ile güncelleyiniz.
markalar[2]="TOGG"
print(markalar)

#5-TOGG listenin bir elemanı mıdır?
print("TOGG" in markalar)

#6-Listenin il 2 elemanını alınız.
sonuc=markalar[0:2]
print(sonuc)

#7-Listenin sonuna "FORD" ve "CITROEN" markalarını ekleyiniz.
sonuc=markalar+["FORD"+"CITROEN"]
print(sonuc)

"""

#8-Listenin son elemanını siliniz.
del markalar[-1]
print(markalar)

#9-Aşağıdaki verileri liste içerisinde saklayınız
"""
ogrenci1:Yiğit Bilgi 2010 [70,80,90] 
ogrenci2:Ada Bilgi 2011 [70,70,80] 
ogrenci1:Çınar Turan 2017 [60,60,90] 
"""
ogrenciler=[["Yiğit","Bilgi",2010,70,80,90],["Ada", "Bilgi", 2011,70,70,80],["Çınar", "Turan", 2017, 60,60,90]]
print(ogrenciler)

#10-Öğrencilerin yaşlarını hesaplayınız.
yil=2025
ogr1Yas=yil-ogrenciler[0][2]
ogr2Yas=yil-ogrenciler[1][2]
ogr3Yas=yil-ogrenciler[2][2]

print("Yiğit:"+str(ogr1Yas)+", Ada:"+str(ogr2Yas)+", Çınar:"+str(ogr3Yas)+" yaşındadır.")

#11-Öğrencilerin not ortalamalarını hesaplayınız.
ogr1Not=ogrenciler[0][3]+ogrenciler[0][4]+ogrenciler[0][5]
ogr2Not=ogrenciler[1][3]+ogrenciler[1][4]+ogrenciler[1][5]
ogr3Not=ogrenciler[2][3]+ogrenciler[2][4]+ogrenciler[2][5]

ort1=ogr1Not/3
ort2=ogr2Not/3
ort3=ogr3Not/3

print("Yiğit:"+str(ort1)+" Ada:"+str(ort2)+" Çınar:"+str(ort3))