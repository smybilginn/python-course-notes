#1-Kendisine gönderilen kelimeyi belirtilen kez ekranda yazdıran fonsiyon
#kelime=input("Yazdırmalk istediğiniz kelime:")
#kacKere=int(input("Kelime kaç kere yazılsın:"))

# def kelimeYaz(kacKere,kelime):
#      i=0
#      while i<kacKere:
#          print(kelime)
#          i+=1
    
# kelimeYaz(kacKere,kelime)
#----------------------------------------------------------------------------------------------------------------------
#2-Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
# kisaKenar=int(input("Kısa kenarı giriniz:"))
# uzunKenar=int(input("Uzun kenarı giriniz:"))

# def dikdortgen(kisaKenar,uzunKenar):
#      return f"Dikdörtgenin Alanı:"+str((kisaKenar*uzunKenar))+" ve dikdörtgenin çevresi:"+str((2*kisaKenar+2*uzunKenar))

# print(dikdortgen(kisaKenar,uzunKenar))
#----------------------------------------------------------------------------------------------------------------------
#3-Yazı-Tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
# def yaziTura():
#     import random
#     sayi=random.random()

#     if sayi<0.5:
#         return "Yazı"
#     else:
#         return "Tura"

# sonuc=yaziTura()
#print(sonuc)
#----------------------------------------------------------------------------------------------------------------------
#4-Kendisine gönderilen iki sayı arasındaki tüm asal sayıları bulan fonsiyon
def asalSayilar(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if(sayi>1):
            for i in range(2,sayi):
                if (sayi%i ==0):
                    break
            else:
                print(sayi)

#asalSayilar(10,20)
#----------------------------------------------------------------------------------------------------------------------
#5-Kendisine gönderilen bir sayının tam bölenlerini liste şeklinde döndüren fonksiyon.
def tamBolenler(sayi):
    bolenler=[]

    for i in range(2,sayi):
        if(sayi%i==0):
            bolenler.append(i)
        
    return bolenler

print(tamBolenler(30))

