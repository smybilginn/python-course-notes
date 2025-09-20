kursAdi="BTK Akademi Python ile Programlama Dersleri"
webSite="https://www.btkakademi.gov.tr/"

"""
#1-' BTK Akademi ' karakter dizininin baş ve sondaki boşluk karakterlerini siliniz.
cumle=" BTK Akademi "
msj=cumle.strip()
print(msj)

"""

"""
#2-kursAdi değişkenindeki tüm karakterleri küçük harfe çeviriniz.
msj=kursAdi.lower()
print(msj)

"""

"""
#3-website değişkeninde kaç tane nokta(.) karakteri vardır?
msj=webSite.count('.')
print(msj)

"""


"""
#4-website değişkeni https ile mi başlıyor?
msj=webSite.startswith("https")
print(msj)

"""

"""

#5-website tr ile mi bitiyor?
msj=webSite.endswith("tr")
print(msj)

"""
"""
#6-kursAdi içerisindeki tüm karakterler haflerden mi oluşuyor?
msj=kursAdi.isalpha)
print(msj)

"""
"""
#7-kursAdi içerisindeki tüm boşlukları "-" ile değiştir.
msj=kursAdi.replace(" ","-")
print(msj)

"""

"""

#8-kursAdi içerisindeki Python kelimesini ReactJs ile değiştir.
msj=kursAdi.replace("Python","ReactJs")
print(msj)

"""
"""
#9-webSite değişkeni "www" içeriyor mu?
msj=webSite.find('www') #içerdiği durumda index numarasını verir. içermediği durumda -1 döndürür.
msj1=webSite.index('aaa') #içerdiği durumda index numarasını verir içermediğinde hata fırlatır.
print(msj1)

"""

"""
#10- kursAdi değişkenini listeye çeviriniz
msj=kursAdi.split()
print(msj)

"""