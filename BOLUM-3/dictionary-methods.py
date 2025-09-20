#Dictionary Metdodları
yemekTarifi={
    "yemekAdi":"Musakka",
    "yemekTarifi":"Yemek tarifi",
    "resim":"1.jpg"
}

#access items
sonuc=yemekTarifi["yemekAdi"]
sonuc=yemekTarifi.get("yemekAdi")
sonuc=yemekTarifi.keys() #tüm keyleri listeyi getirir
sonuc=yemekTarifi.values() #tüm value değerleri liste olarak getirir.
sonuc=yemekTarifi.items() #dictionary to liste

#Update items
yemekTarifi["yemekAdi"]="Mantı"
yemekTarifi.update({"yemekAdi":"Mantı"}) #değeri değiştirir.
yemekTarifi.update({"yemekAdi2":"Çorba"}) #aynı değerden varsa sona ekleme yapar.

#delete items
#yemekTarifi.pop("yemekAdi") #parametre olarak gönderilen değeri siler
yemekTarifi.popitem() #parametre almaz.
yemekTarifi.clear() #listedeki tüm elemanları siler.

#copy => referans

sonuc=yemekTarifi
print(sonuc)