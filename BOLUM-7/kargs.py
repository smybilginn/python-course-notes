def display_user(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    print("\n")

display_user(username="sumeyyebilgin")
display_user(username="sumeyyebilgin",email="info@sumeyyebilgin.com")

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value1",key2="value2")
