def result(guj,gk,eng,math):
    print("guj",guj)
    print("gk",gk)
    print("eng",eng)
    print("math",math)
    
    total=math+eng+guj+gk
    return total
  
math=40
guj=50
eng=57
gk=46
#without keyword argument: res=result(math,guj,eng,gk)

#with keyword argument:
res=result(math=math,guj=guj,eng=eng,gk=gk)

print(res)