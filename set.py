
l1 = {10,20,50,80}
print(l1)
l2 = {10,30,40,60}
print(l2)
l3 = l1.intersection(l2)
print(l3)

print("==============================================")

s1 = {10,30,50,90}
print(s1)
s2 = {10,30,50,90,100,60}
print(s2)
s3 = s2.issubset(s1)
print(s3)

print("=====================================")

a = {10,25,45,56}
print(a)
b = {10,25,45,56}
print(b)
c = a.issuperset(b)
print(c)

print("====================================================")


a = {90,12,4,68}
print(a)
b = a.pop()
print(b)
c = a.pop()
print(c)
d = a.pop()
print(d)
e = a.pop()
print(e)
f = a.pop()
print(f)
print("====================================================================")

d = {10,20,50,80,60}
d.remove(60)
print(d)
