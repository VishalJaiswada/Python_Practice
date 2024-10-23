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

f=open("fileI_O.txt","r")
data=f.read()
print(data)
print(type(data))
