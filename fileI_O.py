# File I/O in python ,Lec-7

# Types of files -->
# 1) Text files: .txt , .docx , .log etc
# 2) Binary files: .jpg , .png , .mp4 ,.mov etc

# operations are performed on the file system-->
# Open , read & close File 

# f= open("file_name","mode")
#           |           |
#           sample.txt   r:read Mode ,w: write mode
#           demo.docx    

## Coding Example

# f=open("fileI_O.txt","r")
# data=f.read()   #read entire file
# print(data)
# print(type(data))
# f.close()

# f=open("fileI_O.txt","r")
# data=f.read(20) #read specified character file 
# print(data)
#f.close()

f=open("fileI_O.txt","r")
line1=f.readline() #read specified line 
print(line1)

line2=f.readline() #read specified line
print(line2)

line3=f.readline() #read specified line
print(line3)

line4=f.readline() #read specified line
print(line4)

f.close()
 