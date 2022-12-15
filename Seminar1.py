# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

import random

lst=[i for i in range(10)] # Создали список из чисел до 10
lst.pop(random.randint(0, 9))
print(*lst)
search_num = 0

for i in range(len(lst)):
    if lst[i]-lst[i-1]>1:
        print(i)
        search_num = i

with open ('file1.txt', 'w') as file:
    file.write(' '.join(list(map(str, lst))))    

with open ('file1.txt', 'r') as file:     
    lst_new = file.read().split()
    print(*lst_new)

lst_new.insert(search_num, search_num)    
print(*lst_new)

with open ('file1.txt', 'a') as file:
    file.write('\n' + ' '.join(list(map(str, lst_new))))