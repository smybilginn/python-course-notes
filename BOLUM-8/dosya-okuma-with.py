# file=open("log.txt",encoding="utf-8")

# print(file.read())

# file.close() #dosyayı kappatı. Bellekte yer kaplamasın.

#with open("log.txt",encoding="utf-8") as file:  #with kullanıldığınd aher seferinde close yapılmak zorunda kalınmaz.   Otomatik olarak kendisi kapatır.
    # print(file.read(10)) #10 karakter oku
    # print(file.tell()) #cursor konumunu getirir.

try:
    with open("log2.txt",encoding="utf-8") as file:
        for i in file:
            print(i,end="") #end="" boş satırı atladı

except FileNotFoundError as e:
    print("Dosya okuma hatası")