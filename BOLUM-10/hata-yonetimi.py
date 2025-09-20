while True:
    try:
        x=int(input("x sayısı:"))
        y=int(input("y sayısı:"))

        print(x/y)

    except (ZeroDivisionError,ValueError) as e:
        print("x ve ye bir sayı olmalıdır.Sıfır olamaz!")
        print(e)

    except Exception as e:
        print("Bilinmeye bir hata oluştu")
        print(e)

    else:
        break

    finally:
        print("finally bloğu çalıştı.")