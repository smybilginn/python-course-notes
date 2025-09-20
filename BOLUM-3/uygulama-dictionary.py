#Aşağıdaki öğrenci bilgilerini dictionary listesinde saklayınız.
    #101 Yiğit Bilgi 2010 (40,80,90)
    #102 Ada Bilgi 2012 (80,80,90)
    #103 Çınar Turan 2017 (70,70,70)

ogrBilgi={
    101: {
        "Ad":"Yiğit",
        "Soyad":"Bilgi",
        "DogumYili":2010,
        "Notlar":(40,80,90)
    },
    102:{
         "Ad":"Ada",
        "Soyad":"Bilgi",
        "DogumYili":2012,
        "Notlar":(70,70,70)
    },
    103:{
         "Ad":"Çınar",
        "Soyad":"Turan",
        "DogumYili":2017,
        "Notlar":(40,80,90)
    }
}
print(ogrBilgi)

#Klavyeden girilen öğrenci numarasına göre aşağıdaki cümleyi yazdırınız.
#101 numaralı Yiğit Bilgi öğrencinin yaşı 14 not ortalaması 70 tir.

ogrNo=int(input("Öğrenci numarası giriniz: "))
ogrenci=ogrBilgi[ogrNo]
ortalama=((ogrenci["Notlar"][0])+(ogrenci["Notlar"][1])+(ogrenci["Notlar"][2]))/3

print(f"{ogrNo} numaralı {ogrenci["Ad"]} {ogrenci["Soyad"]} isimli öğrencinin yaşı {2025-ogrenci["DogumYili"]} not ortalaması {ortalama} ")
    