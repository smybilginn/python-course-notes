#for list
sayilar=[1,5,7,89,52]
isimler=["ali","zeynep","ayşe"]
adSoyad="Sümeyye Bilgin"

# for x in sayilar:
#     print(x)

 
# for isim in isimler:
#     print(isim)

# for i in adSoyad:
#     print(i)

# my_tuple=[(1,2),(3,4),(5,6)]

# for a,b in my_tuple:
#     print(a,b)

my_dict={"41":"Kocaeli","53":"Rize","35":"İzmir"}

# for i in my_dict:
#     print(i)

# for i in my_dict:
#     print(my_dict[i])

for i in my_dict.values(): #.value sadece değerleri getirir.
    print(i)

for i in my_dict.keys():   #.keys sadece anahtar kelimeri geririr.
    print(i)

for a,b in my_dict.items(): #.items key ve value'ları birlikte getirir.
     print(a,b)