import os

path = 'E:\專題\Pixnet\新竹景點'

f=os.listdir(path)
nums = len(f)
print(nums, type(nums))
for n in range(0,nums):
    oldname = f[n]
    print('舊檔名:', oldname) #___________舊檔名有副檔
    name = oldname.split('.txt')
    # print('舊名無副檔名:', name[0]) #___________舊名無副檔名
    newname = name[0] + '.json'
    print('新檔名:', newname) #___________新檔名
    os.chdir(path)
    os.rename(oldname, newname)
