import os

import shutil

TARGET = "backupfolder"
os.chdir(TARGET)

print(os.getcwd())

#Returns list of files in current working directory
fileNames = os.listdir(".")

for file_ in fileNames :
    # print(file_)
    # print(file_.split(".")[-1])
    dirName = file_.split(".")[-1]
    # print(dirName)
    os.makedirs(dirName, exist_ok=True)
    src = file_
    dst = os.path.join(dirName,file_)
    # print(src, dst)
    shutil.move(src,dst)


    # print(file)