import os
import time
start = time.time()

count=1 #Показывает какая пара по счету будет изменяться
i=0 #Счетчик
n=0 #Счетчик промежуточных пар который стремится к tempk
finalbuffer= ""  #итоговая строка
buffer_len = 1    # максимальный размер рабочего буфера
tempk=0 #временное значение переменной k (глобальная)
preview=""   #Предыдущий символ
a=1

try:
    with open("text.txt", 'r') as file:
        buffer = file.read(buffer_len)
        if not buffer:
            print("\nФайл .txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:
            a=-a
            while buffer == "0":
                tempk+=1
                buffer=file.read(buffer_len)
                count=tempk
                preview=""


            n += 1
            if n//2 == count:
                n=0
                if preview.isdigit() == True and buffer.isdigit() == False:
                    finalbuffer += str(preview)
                    buffer = file.read(buffer_len)
                elif preview.isdigit() == True and buffer.isdigit() == True:
                    finalbuffer += buffer + preview
                    buffer = file.read(buffer_len)
                    preview=buffer

            elif count > 1 and n > 1:
                if preview.isdigit() == True and buffer.isdigit() == False:
                    finalbuffer += str(preview)
                    buffer = file.read(buffer_len)
                elif preview.isdigit() == True and buffer.isdigit() == True:
                    finalbuffer += preview + buffer
                    buffer = file.read(buffer_len)
                preview = buffer
                buffer = file.read(buffer_len)
                n+=1
            else:
                preview = buffer
                buffer = file.read(buffer_len)

            tempk = 0
        if a == 1:
            finalbuffer+=preview
        finalbuffer=finalbuffer.replace("0","")
        print(finalbuffer)
except ValueError:
    print("Файл .txt содержит символы. Откорректируйте файл text.txt в директории или переименуйте существующий *.txt файл")