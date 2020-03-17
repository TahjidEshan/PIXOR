from os import listdir
from os.path import isfile, join

mypath = "/mnt/hdd1/lxc-hdd1/tahjid/KITTI/training/velodyne"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(len(onlyfiles))
items = len(onlyfiles)
traincount = int(items*(80/100))
valcount = items - traincount
trainitems = onlyfiles[:traincount]
valitems = onlyfiles[traincount+1:]
f= open("train.txt","w+")
for i in trainitems:
    f.write(f"{i.replace('.bin', '')}\n")
f.close()
f= open("val.txt","w+")
for i in valitems:
    f.write(f"{i.replace('.bin', '')}\n")
f.close()