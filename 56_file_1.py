#read content from file
filename = 'country.txt'
mode = 'r'
file = open(filename,mode) 
#display content of file line by line 
#count how many lines in file 
count = 0
for line in file:
    print(line.strip())
    count+=1
file.close()
print(f"this file has {count} lines")