filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames=[]
for index,item in enumerate(filenames):
    x,y = item.split(".")
    if y=="hpp":
        newitem = x+".h"
    else:
        newitem=item
    newfilenames.append((item,newitem))
print(newfilenames)


    
