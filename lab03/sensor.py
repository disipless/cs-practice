
degrees_lim = float(input('Введите лимит температуры в градусах цельсия: '))
count_lines = int(input('Введите количество записей: '))

count_lim = 0
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

for i in range(count_degrees):
    if degrees_mas [i] > degrees_lim:
        count_lim += 1


print(f'{count_lines}\n{ceror}\n{count_lim}\n{max(degrees_mas):.1f}\n{(sum(degrees_mas))/(count_degrees):.1f}')
