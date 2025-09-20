# file=open("dosya.txt","w",encoding="utf-8")

# file.write("Sümeyye Bilgin\n")
# file.write("Ezgi Bilgin")

# file.close()

with open("dosya.txt","w",encoding="utf-8")as file:
    file.write("Sümeyye Bilgin\n")
    file.write("Ezgi Bilgin\n")

with open("dosya.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i,end="")