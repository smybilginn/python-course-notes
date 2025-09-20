liste = ["1","3","5","20b","abc","10a","60"]
# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# for x in liste:
#     try:
#         sonuc = int(x)
#         print(sonuc)
#     except ValueError:
#         continue

# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.
# while True:
#     sayi=input("Sayı:")
    
#     if sayi=="q":
#         break
    
#     try:
#         sonuc= float(sayi)
#         print(f"girilen sayı:{sonuc}")
#         break
#     except ValueError:
#         print("geçersiz sayı")
#         continue


#3: Dictonary ve key bilgilerini parametre olaran alan get(dict,key) fonksiyonu hazırlayınız.
urun = {"urunAdi":"samsung s20","fiyat":10000}

# d["fiyat"] => KeyError

# get(urun, "fiyat")   => None
# get(urun, "urunAdi") => samsung S20

def get(liste, key):
    try:
        return liste[key]
    except KeyError:
        return None
    

sonuc = get(urun, "fiyat")
sonuc = get(urun, "urunAdi")

print(sonuc)
