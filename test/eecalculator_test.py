import os
PackagePath="EECalculator"
MenuList=[]
for i in os.listdir(PackagePath):
    if os.path.isdir(os.path.join(PackagePath,i)):
        MenuList.append(i)
print(MenuList)