sayilar=[3,5,7,2,12,32,45]

#1-Sayılar listesindeki her bir elemanı yazdırınız.
# for i in sayilar:
#     print(i)

#2-sayilar listesinde hangi sayılar 3'ün katıdır?
# for i in sayilar:
#     if(i%3==0):
#         print(i)
    
#3-sayilar listesindeki tüm sayiların toplamı nedir?
# toplam=0
# for i in sayilar:
#     toplam+=i
# print(toplam)

urunler=["samsung s24","samsung s22","iphone 15","iphone 14"]

#4-urunler listesndeki tüm iphone ürünleri listeleyin.
# for i in urunler:
#     index=i.find("iphone") #find true durumda 0, false durumda -1 döndürür.
#     if(index>-1):
#         print(i)

#urunler listesinde kaç samsung ürünü vardır?
adet=0

for i in urunler:
    index=i.find("samsung")
    if(index>-1):
        adet+=1
print(adet)