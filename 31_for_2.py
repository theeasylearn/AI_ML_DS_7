# how to use for loop with tuples 
nums = (34,-12,57,-83,19,-45,76,-98,41,-67,23,-54,88,-29,62,-71,15,-93,48,-36,91,-58,27,-84,73,-47,56,-92,18,-63,81,-25,44,-79,67,-31,12,-88,95,-53,29,-76,63,-41,87,-19,52,-69)
#count how many negative & positive values 
negative = 1
positive = 1
for item in nums:
    # print(item)
    if item<0: 
        negative+=1
    else: 
        positive+=1

print("positive =",positive)
print("negative =",negative)

#task
#generate and display total of positive value
#generate and display total of negative value

#count odd values 
#count even values 
# generate and display total and average if item is negative convert it into positive
#   