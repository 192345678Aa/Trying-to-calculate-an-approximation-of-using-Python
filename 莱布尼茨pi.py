pi=0
for number in range(1,500000,4):
    pi= pi+1/number
for numbera in range(3,500000,4):
    pi= pi-1/numbera
print(pi*4)