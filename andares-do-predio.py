#Opção com For
for i in range(21):
    if(i == 13):
        continue
    print(i)

#Opção com while

i = 0
while i < 21:
    if i != 13:
        print(i)
    i += 1

print('-' * 10)

#Imprimindo em ordem decrescente

for cont in range(20, -1, -1):
    if(cont == 13):
        continue
    print(cont)
