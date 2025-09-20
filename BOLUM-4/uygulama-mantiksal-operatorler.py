#1-Yaşı 18 den büyük ya da veli izni varsa çalışabilir durumunu kontrol ediniz.
yas=int(input("Yaş giriniz:"))
izin=input("İzin var mı:")

sonuc=(yas>18) and (izin=="Evet")

print("Sonuç: "+str(sonuc))

#2-Ders notu 50-100 arasında ise geçti değilse kaldı bilgisini yazdırınız.
DersNot=int(input("Not giriniz:"))
sonuc=DersNot>=50 and (DersNot<=100)

print(sonuc)

#3-Not ortalaması en az 70 ve zayıfı yoksa teşekkür alabilme durumunu kontrol ediniz
not1=int(input("1. not:"))
not2=int(input("2. not:"))
not3=int(input("3. not:"))

notOrtalama=(not1+not2+not3)/3

print((not1>=50 and not2>=50 and not3>=50) and notOrtalama>=70) 

#4-İşe girmek için en az ön lisans yada lisans mezunu olma durumunu kontrol ediniz.Sigara kullanmama koşulu var.
durum=input("Ön lisans/Lisans mezuniyet durumu giriniz:")
sigara=input("Sigara kullanıyor musunuz?")

print((durum=="Ön lisans" or durum=="Lisans" and sigara=="Hayır"))

# #5-Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.
email="info@sadikturan.com"
userName="sadikturan"
password="12345"

girisBilgisi=input("userna veya e-posta aderesinizi giriniz:")
girisParola=input("Parolanızı giriniz:")
sonuc=(email==girisBilgisi or userName==girisBilgisi) and password==girisParola

print(sonuc)
