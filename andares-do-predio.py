for i in range(21):
    if(i == 13):
        continue
    print(i)

print('-' * 12)

i = 0
while i < 21:
    if i != 13:
        print(i)
    i += 1  # Incrementa 'i' em todas as iterações, no final

print('-' * 10)

for cont in range(20, -1, -1):
    if(cont == 13):
        continue
    print(cont)
