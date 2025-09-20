# for i in range(1,100,2): #1'den başlayıp 100'e kadar giden ve 2 şer olarak artan bir liste getirir.
#     print(i)

rng=range(10) #0'dan 10'a kadar oluşturur.
rng=range(10,20) #10'dan 20'ye kadar oluşturur. 20 dahil değil
rng=range(0,-20,-1) #0'dan -20'ye kadar -1 artırarak listeyi oluşturur.

sonuc=list(rng)
print(sonuc)

for i in range(50,250):
    if i%2==0:
        print(i)