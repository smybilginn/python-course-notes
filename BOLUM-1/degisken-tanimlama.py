#Hesaplama Yöntemleri..

urunAFiyat=2000
urunBFiyat=3000
kdvOrani=0.18

print(urunAFiyat+(urunAFiyat*kdvOrani))
print(urunBFiyat+(urunBFiyat*kdvOrani))

toplamUrunFiyat=urunAFiyat+urunBFiyat

print("ürün fiyat:", toplamUrunFiyat+(toplamUrunFiyat*kdvOrani))
#print(f"Ürün Fiyat: {toplamUrunFiyat+(toplamUrunFiyat*kdvOrani)} ")
#print("Ürün Fİyat: "+ str(toplamUrunFiyat+(toplamUrunFiyat*kdvOrani)))