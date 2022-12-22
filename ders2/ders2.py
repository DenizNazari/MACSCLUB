# a=[1,2,3,"sds",True]
# b=["a","b","c"]
# print(a+b)
# print(a[::-1])
# print(a[0:3]+b+a[3:])
# a="1" in a
# print(a)
a=[1,2,3,4,5]
b=sum(a)
print(b)
a.insert(3,5)
print(a)
a[4]=7
print(a)
print(max(a))
a.insert(-1,7)
print(a)
a.pop(3)
print(a)
# a.remove(7)
# print(a)
# a.sort()

# print(a)
v=a.count(7)
print(v)
v=a.index(3)
print(v)
A=[1,2,3]
# a=tuple(A)
# b=(4,5,6)
# print(a[2])
# c=a+b
# b
print(A*3)
A={
    1234:
        {
    "isim":"Deniz",
   "YAS":20,
   "universite":"esogu",
        },
   
    1356:{
    "isim":"ALI",
   "YAS":25,
   "universite":"esogu",
},
    }
  

# b=[{1234:
#         {
#     "isim":"Deniz",
#    "YAS":20,
#    "universite":"esogu",
#         }},
# {1235:
#         {
#     "isim":"Deniz",
#    "YAS":20,
#    "universite":"esogu",
#         }}
# ]
A.update({1235:{
    "isim":"ALI",
   "YAS":56,
   "universite":"esogu",
},})
print(A)
G=A.copy()


meyveler={"cilek","muz","mandalina","elma"}
telefon={"samsung","apple","mi"}
meyveler.add("armut")
print("cilek" in meyveler)
meyveler.update(telefon)
meyveler.discard("muz")
print(meyveler)
sonuc=len(meyveler)
print(sonuc)
a={1,2,3,4,5,6}
b={4,5,7,8}
sonuc=a.union(b)
print(sonuc)

l,*b,c=4,5,6,7,8

a,d=7,8
a,d=d,a
a%=5
print(b)


a=[11,2,3,4,5]
d=[11,2,3,4,5]
# b=int(input(""))
# c=int(input(""))
# ==
#>=
# d=c>b and a==b 
# [11,2,3,4,5] is a
print(8 not in d)


a=input("a?")
b=input("b?")
c=input("c?")
d=input("d?")
f=[a,b,c,d]
if("x" in f):
      print("sisteme giris yapdiniz")
      f=7
elif("c" not in f):
      print("gizli hesaba girdiniz")
else:
  print("bi daha dene")