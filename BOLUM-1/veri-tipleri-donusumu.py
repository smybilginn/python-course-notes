# sayi1=int(input("sayı 1: "))
# sayi2=int(input("sayi 2: "))

# toplam=sayi1+sayi2

# print(toplam)

# dışarıdan str şeklinde alınan inputu int değere çevirdik.

#--------------------------------------------------------------

# sayi1=(input("sayı 1: "))
# sayi2=(input("sayi 2: "))

# toplam=sayi1+sayi2

# print(toplam)

# inputtan gelen değer her zaman str olarak gelir. farklı bir işlem için tür dönüşümü gerekir.

#------------------------------------------------------------------------------------------------

#x=int("10") str değer int çevrildi

#------------------------------------------------------------------------------------------------
#x=int("10.5") 10.5 float  bir sayı o yüzden çeviremedi. hata verdi

# x=int(10.5)

#   "10.5" burada bir string'dir. Yani "abc" ya da "hello" gibi harfli bir metinden farksızdır.

# int() fonksiyonu string alabilir ama sadece TAM SAYI formatında bir string:

# "10.5" string olarak ondalıklı sayı formatında ve bu, int() için geçersizdir.

# Çünkü int() string'ten sayı üretirken, her karakterin bir tam sayı ifadesi olması gerekir. Nokta (.) gibi karakterler tam sayılarda yer almaz.


# Eğer "10.5" string'ini tam sayıya çevirmek istiyorsan, önce float'a çevirip sonra int yapmalısın:

# x = int(float("10.5"))  # float("10.5") → 10.5 → int(10.5) → 10

#------------------------------------------------------------------------------------------------------------

#x=int(10.5) hatasın çalışır.
#x=float("10") 10.0 olarak çıkar
#x=float("10.4") 10.4
#x=str(3.4) 3.4
x=str(True)
print(type(x))