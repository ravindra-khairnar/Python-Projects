import os

def DirectoryScanner(DirectoryName = "Marvellous"):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such Directory")
        return

    print("Contents of the directory are : ")
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder Name : ", FolderName)
        for subf in SubFolderName:
            print("Sub Folder Name : ", subf)
        for fname in FileName:
            print("File Name : ",fname)

def main():
    DirectoryName = input("Enter the name of directory ")
    DirectoryScanner(DirectoryName)


if __name__ == "__main__":
    main()