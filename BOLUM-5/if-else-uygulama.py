
#Bir öğrencinin iki yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.
#0-24  =>0
#25-44 =>1
#45-54 =>2
#55-69 =>3
#70-84 =>4
#85-100=>5

not1=int(input("1. yazılı notunuz:"))
not2=int(input("2. yazılı notunuz:"))
sozlu=int(input("Sözlü notu giriniz:"))

ortalama=(not1+not2+sozlu)/3
print(f"Ortalama: {ortalama}")

if(ortalama>=0 and ortalama<=24):
    print("Not:1")
elif(ortalama>=25 and ortalama<=44):
    print("Not:1")
elif(ortalama>=45 and ortalama<=54):
    print("Not:2")
elif(ortalama>=55 and ortalama<=69):
    print("Not:3")
elif(ortalama>=70 and ortalama<=84):
    print("Not:4")
elif(ortalama>=85 and ortalama<=100):
    print("Not:5")
else:
    print("Yanlış değer girildi.")