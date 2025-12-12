#example of for loop on list 
countries = ["Egypt","Ireland","Kazakhstan","Finland","Myanmar","Iceland","Indonesia","Pakistan","Japan","Switzerland","Thailand","Bangladesh","Turkey","Vietnam","China","Nepal","Netherlands","Malaysia","Sri Lanka","Kyrgyzstan","Bhutan","Singapore","Poland","Philippines","Cambodia","Uzbekistan","India","Laos","Afghanistan"]
#count how many items list has 
count = 1 
for item in countries:
    print(item)
    count=count+1
print("no of countries =",count)

#print countries ends with land
for item in countries:
    if 'land' in item:
        print(item)

#task
# count how many countries ends with tan and also display it 