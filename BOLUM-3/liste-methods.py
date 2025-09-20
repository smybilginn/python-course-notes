sayilar=[1,3,2,4,5,6,4]
isimler=["Ahmet","Ceyda","Deniz","Zeynep","Aydın"]

sonuc=min(sayilar) #Listedeki en küçük sayıyı getirir.
sonuc=min(isimler) #Listedeki alfabetik olarak en önceki ismi getirir.
sonuc=max(isimler) #Listedeki alfabetik olarak en son ismi getirir.
sonuc=max(sayilar) #Listedeki en büyük sayıyı getirir.

"""
#Ekleme
sayilar.append(15)      #Listenin sonuna 15 sayısını ekler
isimler.append("aydan") #Listenin sonuna aydan ismini ekler 
#sonuc=isimler
sayilar.insert(0,100)   #Lisyenin 0. indexine 100 elemanını ekledi.
sayilar.insert(-1,100)  #Listenin sonuna eklemez!sondaki elemanı bir sağa kaydırıp ekler.
sayilar.insert(-3,100)
sonuc=sayilar
print(sonuc)

"""
"""
#Silme
sayilar.pop(0)             #pop verilen index numarasına göre istenilen elemanı siler.
isimler.remove("Ceyda")    #remove içerisine yazılan elemanı dizide arayıp bulunca siler.
#sonuc=sayilar
sonuc=isimler
print(sonuc)

"""

"""
#Sıralama
isimler.sort()    #Artan sırada sıralama yapar
sayilar.sort()
isimler.reverse()
sayilar.reverse() #Azalan sırada sıralama yapar
sonuc=sayilar

print(sonuc)

"""

"""
#Count
sonuc=sayilar.count(4)      #Listede kaç tane 4 olduğunu sayar.
sonuc=isimler.count("Ceyda")

print(sonuc)

"""

#Arama
sonuc=sayilar.index(4) #4 elemanının kaçıncı indexte olduğu bilgisini verir.

print(sonuc)