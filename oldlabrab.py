import os
import time
start = time.time()
k=1 #Показывает какая пара по счету будет изменяться
i=0 #Счетчик
n=0 #Счетчик промежуточных пар который стремится к tempk
finalbuffer= ""  #итоговая строка
max_buffer_len = 100    # максимальный размер рабочего буфера
maxbuffererror_Flag=False #Идентификатор превышения размера рабочего буффера
def zeroscount(content,i): #функция считающая tempk
    tempk = 0  #временное значение переменной k
    while i<len(content) and content[i]=="0":
        tempk+=1
        i+=1
    return tempk



try:
    with open("text", 'r') as file:
        content = file.read(max_buffer_len)
        if not content:
            print("\nФайл .txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while content:

            while i < (len(content)-1):
                digit=int(content[i])   #поиск неверных элементов
                n+=1
                if n>k:   #сброс счетчика промежуточных пар
                    n=1

                if content[i]!="0" and content[i+1]!="0" and n==k:
                    finalbuffer += content[i + 1] + content[i]
                elif content[i]!="0" and content[i+1]!="0":
                    finalbuffer += content[i] + content[i + 1]
                if content[i+1]=="0" and content[i]!="0":
                    finalbuffer += content[i]
                    i+=1
                if content[i]=="0":
                    k=zeroscount(content,i)
                    i+=k-2
                    n=0
                if i+1==len(content):
                    finalbuffer+=content[i]
                if len(finalbuffer) >= max_buffer_len:
                    print("\nФайл .txt содержит блок цифр, превышающий максимальный размер буфера = " + str(max_buffer_len) + " символов.\nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
                    maxbuffererror_Flag=True
                    break
                i+=2
            if len(content)%2==1:  #При нечетном количестве пар, будет выводиться последний элемент
                finalbuffer+=content[len(content) - 1]
            finish=time.time()
            content=False
            if maxbuffererror_Flag==False:
                print(finalbuffer)
            print("Program time", finish-start, "seconds")
except ValueError:
    print("Файл .txt содержит символы. Откорректируйте файл text.txt в директории или переименуйте существующий *.txt файл")