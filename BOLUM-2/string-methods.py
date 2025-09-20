mesaj=" BTK Akademi Python Kursu"

#msj=mesaj.upper() #Bütün harfleri büyük yapar.
#msj=mesaj.lower() #Hepsi küçük harf olur
#msj=mesaj.title() #Tüm kelimelerin ilk harfini büyütür.
#msj=mesaj.capitalize() #Metnin sadece ilk harfini büyük yapar.

#Soru Gibi
#msj=mesaj.isupper() #Harflerin hepsi büyük mü? True yada False döner
#msj=mesaj.islower()  #Harflerin hepsi küçük mü? True yada False döner

#msj=mesaj.strip() #Metnin başındaki boşluk karakterini siler.
#msj=mesaj.split() #Boşluk karakterini ayırarak metni listeye çevirir.
#msj=mesaj.index("Akademi") #Hnagi indexten başladığını gösterir.
#msj=mesaj.startswith("a") #Metnin hangi harf ile başladığını sorgular. True yada False döner.
#msj=mesaj.endswith("u") #Metnin hangi harf ile bittiğini sorgular.True yada False döner.
msj=mesaj.replace("Python","Java")


print(msj)