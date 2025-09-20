#1-Girilen 2 sayıdan hangisi büyüktür?
# sayi1=int(input("1. sayıyı giriniz:"))
# sayi2=int(input("2. sayıyı giriniz:"))

#print(f"{sayi1} {sayi2} den büyük mü? ",sayi1>sayi2)


#2-Girilen bir sayının tek çift kontrolünü yapınız
# sayi=int(input("Sayı giriniz:"))
# sonuc=sayi%2

# print(f"sayı çift mi? {sonuc==0}")

#3-Bir öğrencinin girilen üç notuna göre başarı durumunu kontrol ediniz. 50 ve üzeri başarılı
not1=int(input("1. notunuzu giriniz:"))
not2=int(input("2. notunuzu giriniz:"))
not3=int(input("3. notunuzu giriniz:"))

ortalama=(not1+not2+not3)/3

print(f"Öğrenci not ortlaması balarılı mı? {ortalama>=50}")