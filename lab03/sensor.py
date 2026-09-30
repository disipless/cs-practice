
degrees_lim = float(input('Введите лимит температуры в градусах цельсия: '))
count_lines = int(input('Введите количество записей: '))
ceror = 0
count_degrees = 0
degrees_mas = []

for _ in range(count_lines):
    degrees = input()
    if degrees == 'error':
        ceror +=1
    else:
        degrees_mas+=[float(degrees)]
        count_degrees +=1


print()