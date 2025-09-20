def toplam():
    return 10+20

sonuc=toplam()
print(sonuc)


def yil():
    import datetime
    return datetime.datetime.now().year


def saat():
    import datetime
    return datetime.datetime.now().hour

def yasHeapla():
    return yil()-1998

print(yasHeapla())

def selamlama():
    if(saat()<12):
        return "Günaydın"
    else:
        return "Merhaba"
    
print(selamlama())