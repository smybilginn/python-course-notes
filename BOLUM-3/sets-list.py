meyveler={"elma","armut","kiraz"}
meyveler2={"ananas","armut","ahududu"}
#sonuc=meyveler[0] #index numarası ile erişilemez.

#for x in meyveler:
#   print(x)

sonuc="kiraz" in meyveler #kiraz elemanını liste içerisinde sorgular. varsa true yoksa false döndürür

meyveler.add("erik") #listeye ekleme yapar
meyveler.update(meyveler2) #iki listeyi birleştirir. Aynı olan elemanlar tekrar yazılmaz.
meyveler.remove("elma") #elmayı siler
meyveler.discard("elma") #remove ile aynı işlemi yapar. Fark: Eğer olmayan bir eleman silinmeye çalışılırsa remove hata fırlatır. 
meyveler.pop() #liste içinden herhangi bir elemanı siler.
meyveler.clear() #liste elemanlarının hepsi silinir.
sonuc=meyveler


print(sonuc)