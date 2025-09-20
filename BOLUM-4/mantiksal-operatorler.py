x=11

#1-and
#True,True   =>True
#True,False  =>False
#False,False =>False

sonuc=(x>5) and (x<10)

#2-or
#True,True   =>True
#True,False  =>True
#False,False =>False

sonuc=(x>0) and (x%2==0) #pozitif çift sayı
sonuc=(x>0) or (x%2==0)  #pozitif veya çift sayı

#3-not
#True  => False
#False => True

sonuc=not(x>10)

print(sonuc)

