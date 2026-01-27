#read content from file
while True:
    try:
        filename = input("Enter file name")
        mode = 'r'
        file = open(filename,mode) 
        content = file.read() #real all lines from file 
        print(content)
        file.close()
        break 
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print("either this is folder or you do not permission to access file")