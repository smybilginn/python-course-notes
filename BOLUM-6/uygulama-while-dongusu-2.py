#Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
#**dictionary listesi yapısı (ogrNo,ogrAd,ogrSoyad) şeklinde olsun
#**ürün ekleme işlemi bittiğinde öğrencileri listeleyiniz.

ogrenciler=[]
devammi="e"
while devammi !="h":
    ogrNo=input("Öğrenci no:")
    ogrAd=input("Öğrenci ad:")
    ogrSoyad=input("Öğrenci soyad:")

    ogrenciler.append({
        "ogrNo":ogrNo,
        "ogrAd":ogrAd,
        "ogrSoyad":ogrSoyad
    }
    )
    devammi=input("Devam mı? (e/h):")

for i in ogrenciler:
    print(f"{i["ogrNo"]} numaralı öğrencinin adı {i["ogrAd"]} {i["ogrSoyad"]} ")


