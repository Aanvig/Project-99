import os
import shutil
import time

deletedFileCount = 0
deletedFolderCount = 0
path = r"C:\Users\pgupta\Desktop\Whitehat\C-99 project\files"
list = os.listdir(path)

day = 30
seconds=time.time()-(30*24*60*60)

def getAge(rootFolder):
    ctime = os.stat(rootFolder).st_ctime
    return ctime

def removeRootFolder(rootFolder):
    if not shutil.rmtree(rootFolder):
        print("Successfully deleted")
    else:
        print("Unable to delete the path")

def removeFolder(Folder):
    if not shutil.rmtree(Folder):
        print("Successfully deleted")
    else:
        print("Unable to delete the path")

def removeFile(files):
    if not os.remove(files):
        print("Successfully deleted")
    else:
        print("Unable to delete")


if os.path.exists(path):
    for rootFolder,folders,files in os.walk(path):
        if seconds >= getAge(rootFolder):
            removeRootFolder(rootFolder)
            deletedFolderCount+=1
            break
        else:
            for folder in folders:
                folderPath=os.path.join(rootFolder,folder)
                if seconds >= getAge(folderPath):
                    removeFolder(folderPath)
                    deletedFolderCount+=1
                    break
            for file in files:
                filePath=os.path.join(rootFolder,file)
                if seconds >= getAge(filePath):
                    removeFile(filePath)
                    deletedFileCount+=1
                    break
else:
    print("Not Found")

print("Number of files deleted: ",deletedFileCount)
print("Number of folders deleted: ",deletedFolderCount)
