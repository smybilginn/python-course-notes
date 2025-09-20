def fullname(firstName: str , lastName: str):
    return f"your name is {firstName} {lastName}"

sonuc=fullname("Sümeyye","Bilgin")
sonuc=fullname(lastName="Bilgin",firstName="Sümeyye")
print(sonuc)