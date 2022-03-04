with open("file.txt",'r') as file:
    content=file.read()
k=1
i=0
n=0
def zeroscount(content,i):
    tempk = 0
    while i<len(content) and content[i]=="0":
        tempk+=1
        i+=1
    return tempk



while i < (len(content)-1):
    n+=1
    if n>k:
        n=1

    if content[i]!="0" and content[i+1]!="0" and n==k:
        print(content[i+1]+content[i], end="")
    elif content[i]!="0" and content[i+1]!="0":
        print(content[i] + content[i+1], end="")
    if content[i+1]=="0" and content[i]!="0":
        print(content[i],end="")
        i+=1
    if content[i]=="0":
        k=zeroscount(content,i)
        i+=k
        n=0
    if i+1==len(content):
        print(content[i],end="")
    i+=2
