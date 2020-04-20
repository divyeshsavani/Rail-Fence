#opens the file file.txt in read mode  
file = open("railfence.txt","r")  
count = 0
content = file.read()
div = "".join(content.split())
"""
print(div)
for i in range(len(content)):
    if(content[i]==" "):
        count=count+1
array1=content+" "
for i in range(count):
        array1=array1+" "
array=""
j=0
for i in range(count+1):
    while array1[j]!=" ":
        array=array+array1[j]
        j=j+1
    j=j+1
"""
n=int(input("Enter key : "))
cipher=""
for i in range(n):
    cipher=cipher+div[i::n]
    i=i+1
print("Plain text \n" + div)
print("Cipher text \n" + cipher)
file.close()