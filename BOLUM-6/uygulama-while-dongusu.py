#1-Başlangıç ve biriş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.
# ilk=int(input("Başlangıç değerini giriniz:"))
# son=int(input("Bitiş değerini giriniz:"))

# i=ilk

# while(i<=son):
#     if((i%2 ==0)):
#         print(i)
#     i+=1

#2-(1-100) arasındaki sayıları azalan şekilde yazdırınız.

# i=100
# while i>=1:
#     print(i)
#     i-=1

#liste metoduyla
# sayilar=[]
# i=100
# while i>=1:
#     sayilar.append(i)
#     i-=1
# print(sayilar)

#3-Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı şekilde yazınız.
# sayi1=int(input("1. sayı:"))
# sayi2=int(input("2. sayı:"))
# sayi3=int(input("3. sayı:"))
# sayi4=int(input("4. sayı:"))
# sayi5=int(input("5. sayı:"))

# sayilar=[sayi1,sayi2,sayi3,sayi4,sayi5]
# # sayilar.sort()
# # print(sayilar)

#2. Yöntem
# sayilar=[]
# i=0
# while i<5:
#     sayi=int(input(f"{i+1}. sayıyı giriniz:"))
#     sayilar.append(sayi)
#     i+=1
# sayilar.sort()
# print(sayilar)

#4-Dışarıdan girilen username bilgisi için boşluk girildiği sürece tekrar username bilgisi isteyiniz.
username="" #buradan bize false döndürür.

while not username:
    username=input("username giriniz:") #false döndüğü sürece döngü devam eder. Karakter girilip true olunca döngü sonlanır.
print("Girilen username:"+username)