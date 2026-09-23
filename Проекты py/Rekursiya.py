import os
path = "C:\\Users\Artem\Pictures\PrRekursiya"
print(os.listdir(path))
def obxod(path,level = 1):
    print("Level = ",level,"Content: ",os.path.isdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+"\\"+i):
            print("Спускаемся",path+"\\"+i)
            obxod(path+"\\"+i,level+1)
            print("Возвращаемся в ",path)
            print(i,type(i),path + "\\"+i,os.path.isdir(path+"\\"+i))
obxod(path)
