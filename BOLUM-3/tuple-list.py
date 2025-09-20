my_list=[1,2,3,4]
my_tuple=(1,2,3,4) #ekleme silme güncelleme işlemleri yapılamaz.

print(type(my_list))
print(type(my_tuple))

my_list[0]=5
#my_tuple[0]=5 hatalı

sonuc=my_list
print(sonuc) 

my_list.append(3)
#my_tuple.append(3) hatalı

#Tuple da kullanılabilecek methodlar
print(my_tuple.count(4))
print(my_tuple.index(2))

#Tür Dönüşümü
my_tuple2=tuple([1,2,3])
my_list2=((1,2,3))