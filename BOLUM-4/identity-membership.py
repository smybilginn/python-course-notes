x=[2,4,6]
y=[2,4,6]
z=y 

print(x==y)
print(x is y)       #nesne benzerliğini kontrol eder.
print(x is not y)   #nesne benzerliğini kontrol eder.

print(z is y)       #nesne benzerliğini kontrol eder.
print(z is not y)

#membership
print(20 in x)      #varlık kontrolü yapar.
print(20 not in x)