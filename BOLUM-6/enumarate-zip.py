#markalar=["bmw","opel","togg"]

# index=1

# for marka in markalar:
#     print(f"{index} {marka}")
#     index+=1

# obj1=enumerate(markalar,1)
# print(type(obj1))
# print(list(obj1))

# for index,marka in enumerate(markalar,1):
#     print(f"{index} {marka}")

#Zip : Elimizde birden fazla liste varsa birleştirmek içi kullanılır.
numara=[100,200,300]
ogrenci=["Ali","Ayşe","Fatma"]

print(list(zip(numara,ogrenci))) #for döngüsü dışında kullanılacaksa list'e çevrilmeli

for no,isim in zip(numara,ogrenci):
    print(no,isim)