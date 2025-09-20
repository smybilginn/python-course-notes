"""
** BankaHesabi isminde bir sınıf tanımlayınız.
** Üretilen her bir nesne "hesapSahibi" isminde biz özelliğe sahip olmalıdır. BankaHesabi("Sadık Turan")
** Üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
** Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp bakiye
   üzerine ekleyin ve bakiye miktarını geriye döndürün.
** Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiye
   değerinden çıkarıp geriye döndürün.

"""

class bankaHesabi:
    def __init__(self,hesapSahibi):
      self.hesapSahibi =hesapSahibi
      self.bakiye=0.0

    def paraYatir(self,miktar):
       self.bakiye+=miktar

       return self.bakiye
    
    def paraCek(self,miktar):
       if miktar>self.bakiye:
          return f"Bakiye yetersiz"
       else:
          self.bakiye-=miktar
          return self.bakiye
       
hesap1 = bankaHesabi("Sümeyye")

# Sürekli işlem döngüsü
while True:
    print("\n1- Para Yatır\n2- Para Çek\n3- Çıkış")
    islem = input("İşlem seçin: ")

    if islem == "1":
        tutar = float(input("Yatırmak istediğiniz tutarı giriniz: "))
        yeni_bakiye = hesap1.paraYatir(tutar)
        print(f"Yeni bakiye: {yeni_bakiye} TL")
    elif islem == "2":
        tutar = float(input("Çekmek istediğiniz tutarı giriniz: "))
        sonuc = hesap1.paraCek(tutar)
        print(f"Sonuç: {sonuc}")
    elif islem == "3":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem.")

        

   
   
   
      
