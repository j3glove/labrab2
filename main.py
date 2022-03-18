import os
import time
start = time.time()
with open("file.txt",'r') as file:
    content=file.read()
k=1 #Показывает какая пара по счету будет изменяться
i=0 #Счетчик
n=0 #Счетчик промежуточных пар который стремится к tempk
allcontent=""  #итоговая строка
def zeroscount(content,i): #функция считающая tempk
    tempk = 0  #временное значение переменной k
    while i<len(content) and content[i]=="0":
        tempk+=1
        i+=1
    return tempk


try:
    while i < (len(content)-1):
        digit=int(content[i])   #поиск неверных элементов
        n+=1
        if n>k:   #сброс счетчика промежуточных пар
            n=1

        if content[i]!="0" and content[i+1]!="0" and n==k:
            allcontent += content[i+1]+content[i]
        elif content[i]!="0" and content[i+1]!="0":
            allcontent += content[i] + content[i+1]
        if content[i+1]=="0" and content[i]!="0":
            allcontent += content[i]
            i+=1
        if content[i]=="0":
            k=zeroscount(content,i)
            i+=k-2
            n=0
        if i+1==len(content):
            allcontent+=content[i]
        i+=2
    if len(content)%2==1:  #При нечетном количестве пар, будет выводиться последний элемент
        allcontent+=content[len(content)-1]
    finish=time.time()
    print(allcontent)
    print("Program time", finish-start, "seconds")
except ValueError:
    print("Файл text.txt содержит символы. Откорректируйте файл text.txt в директории или переименуйте существующий *.txt файл")