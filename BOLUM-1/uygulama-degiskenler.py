isim="Sadık Turan"
gsmNo="05321234567"
ePosta="info@sadikturan.com"
sehir="Kocaeli"

urun1="Kablosuz Mouse"
urun1Fiyat=550

urun2="Kablosuz Klavye"
urun2Fiyat=650

urun3="Dizüstü Bilgisayar"
urun3Fiyat=55000

kdvOrani=0.18

toplamTutar=(urun1Fiyat+urun2Fiyat+urun3Fiyat)*kdvOrani+(urun1Fiyat+urun2Fiyat+urun3Fiyat)

odenenKdvOrani=(urun1Fiyat+urun2Fiyat+urun3Fiyat)*kdvOrani

print("Müşteri ismi: "+isim)
print("Müşteri Telefon No:", gsmNo)
print("e-posta adresi: ",ePosta)
print("Şehir:", sehir )

print("Satın alınan ürünler: ",urun1+"="+str(urun1Fiyat)+", "+urun2+"="+str(urun2Fiyat)+", "+urun3+"="+str(urun3Fiyat))

print("Toplam="+str(toplamTutar))
print("kdv tutarı: "+str(odenenKdvOrani))
