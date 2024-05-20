a = (1,2,3,4)
b = ("a","b","c")
c = ("小a","小b")
for j,k,l in zip(a,b,c):
    print(j,k,l)

for i in range(min(len(a),len(b),len(c))):
    print(a[i],b[i],c[i])