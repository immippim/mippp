A = ["Pimchanok","Dangsuwan","46505"]
k= A[0]
d= A[1]
f= A[2]
print(k)
print(d)
print(f)

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

Num = int(input('Enter Your Loop'))
NumTotal = []
for i in range(Num):
    data = int(input( 'Enter Your Data: '))
    NumTotal += [data]
print(NumTotal)
NumTotal.sort()
print(NumTotal)