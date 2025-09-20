customers=["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals=[1200,13000,5000,15000]

"""
#1 sadikturan adı ile yapılan 5000 TL'lik siparişi listeye ekleyiniz.
customers.append("sadituran")
order_totals.append(5000)
sonuc=order_totals
sonuc=customers
#print(sonuc)

#2-Son eklenen siparişi siliniz
order_totals.pop()
sonuc=order_totals
print(sonuc)

#3-Tüm müşteriler için aşağıdaki metni yazdırınız
#<username> isimli müşterinin sipariş toplamı <10000> Tl dir.
print(customers[0]+" isimli müşterinin sipariş toplamı "+str(order_totals[0])+" TL'dir.")
print(customers[1]+" isimli müşterinin sipariş toplamı "+str(order_totals[1])+" TL'dir.")
print(customers[2]+" isimli müşterinin sipariş toplamı "+str(order_totals[2])+" TL'dir.")
print(customers[3]+" isimli müşterinin sipariş toplamı "+str(order_totals[3])+" TL'dir.")

ya da

sonucf"{customers[0]} isimli müşterinin  sipariş toplamı {order_totals[0] TL'dir.}

#4-Müşterileri alfabetik olarak sıralayınız.
customers.sort()
print(customers)

#5-Sipariş toplamlarını azalan şekilde sıralayınız
order_totals.sort(reverse=True)
#print(order_totals)

#6-En düşük sipariş hangisidir?
sonuc=min(order_totals)
print(sonuc)

#7-sadituran isimli kullanıcının kaç siparişi var?

sonuc=customer.count("sadikturan)

#8-Customers listesinden ahmetyilmaz isimli kullanıcıyı siliniz.
customers.remove("ahmetyilmaz")
print(customers)
"""
#9 listelerdeki tüm içerikleri siliniz.
customers.clear()
order_totals.clear()

#10-Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını siteye ekleyiniz.
kullaniciAdi=input("Kullanici adı giriniz: ")
siparisToplami=input("Siparis toplamınızı giriniz: ")

customers.append(kullaniciAdi)
order_totals.append(siparisToplami)

print(customers)
print(order_totals)