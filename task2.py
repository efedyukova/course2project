import sys
import os
import re
 

work_file = '/Users/ekaterina/Documents/task2.txt'
#if os.path.isfile(work_file):
    #print('Рабочий файл: ' + work_file)
 
# читаем файл
file = open(work_file,'r', encoding = 'utf-8')
try:
    txt = file.read()
finally:
    file.close()
 
# выбираем слова через регулярные выражения
p = re.compile("([а-яА-Я-']+)")
res=p.findall(txt)
 
# создаем словарь. Ключ-слово, Значение-частота повторения
lsWord = {}
for key in res:
    key = key.lower()
    if key in lsWord:
        value = lsWord[key]
        lsWord[key]=value+1
    else:
        lsWord[key]=1
 
# создаем список ключей отсортированный по значению словаря lsWord
sorted_keys = sorted(lsWord, key=lambda x: int(lsWord[x]), reverse=True)
file = open(work_file+'_dict.csv','a+', encoding = 'utf-8')
try:
    for key in sorted_keys:
        s = str("{0};{1} /n").format(key,lsWord[key])
        file.write(s)
    print('Результат записан: '+work_file+'_dict.csv')
finally:
    file.close()


