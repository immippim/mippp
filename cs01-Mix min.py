Num = int(input('Enter Your Loop'))
NumTotal = []
for i in range(Num):
    data = int(input( 'Enter Your Data: '))
    NumTotal += [data]
NumTotal.sort()
print(NumTotal[0])
print(NumTotal[-1])