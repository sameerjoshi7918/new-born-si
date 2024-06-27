import wikipedia as wd
In = input("Search please : ")
result=wd.summary(In, sentences=3)
print(result)
