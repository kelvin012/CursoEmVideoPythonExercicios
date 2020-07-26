i = s = 0
while True:
    num = int(input('Digite um número </ 999 to STOP /> '))
    if num == 999:
        break
    s += num
    i += 1
print(f'Foram digitados {i} números e a soma de todos eles é igual a {s}')
