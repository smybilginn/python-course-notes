urunler=[
    {"urunAdi":"Hp Victus","fiyat":32999},
    {"urunAdi":"Lenovo ThinkPad","fiyat":25499},
    {"urunAdi":"Apple Macbook","fiyat":49999},
    {"urunAdi":"Huawei Matebook","fiyat":26999},
    {"urunAdi":"Casper Nirvana","fiyat":20000},
]
#1-Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
#Hp Victus marka ürünün fiyatı 32999 Türk Lirası
for i in urunler:
    print(f"{i['urunAdi']} marka ürünün fiyatı {i['fiyat']} Türk Lirasıdır.")

#2-Ürünlerin fiyatları toplamı nedir?
toplam=0
for i in urunler:
    toplam+=i["fiyat"]
print(f"Ürünlerin toplam fiyatı {toplam}")

#3-25000 ile 40000 arasındaki ürünleri listeleyiniz.
for i in urunler:
    if(i["fiyat"]>=20000 and i["fiyat"]<=40000):
        print(i)

#4-Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.
kelime=input("Ürün adı giriniz:")

for i in urunler:
    if(i["urunAdi"].lower().find(kelime.lower())>-1):
        print(f"{i['urunAdi']}")