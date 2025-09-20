def toplam(*args): # '*' dışarıdan değişken sayıda parametre alabilir demek
    print(args)
    print(type(args))
    sonuc=0
    for i in args:
        sonuc+=i
    return sonuc

sonuc=toplam(10,20,30,60)
print(sonuc)