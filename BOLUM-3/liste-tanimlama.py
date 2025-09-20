programlama_dilleri=["Python","Java","C#","Javascript"]

sonuc=programlama_dilleri
sonuc=programlama_dilleri[0:2]
sonuc=programlama_dilleri[:2]
sonuc=programlama_dilleri[:]
sonuc=programlama_dilleri[-3:-1] #bitiş indexi(-1) dahil değil.
sonuc=programlama_dilleri[-3:] #bitiş indexi(-1) dahil.
#print(type(sonuc))


#Güncelleme
sonuc=programlama_dilleri[-1]="Php" #-1.(son) indexi değiştirdik.

sonuc=len(programlama_dilleri) #listenin elemean sayısını verir.

sonuc=programlama_dilleri+["Go","Delphi"] #listeye eleman eklendi.

sonuc="Python" in programlama_dilleri #"Python" ifadesi programlama_dilleri listesinde var mı? true/false

del programlama_dilleri[0] #programlama_dilleri listesinin 0. indexini siler.

for i in programlama_dilleri: #for dögüsü
    print(i)
print(sonuc)
