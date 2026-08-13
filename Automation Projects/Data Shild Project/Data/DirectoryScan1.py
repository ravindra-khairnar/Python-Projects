import os

def main():
    DirectoryName = input("Enter the name of directory")

    print("Contents of the directory are : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder Name : ", FolderName)
        for subf in SubFolderName:
            print("Sub Folder Name : ", subf)
        for fname in FileName:
            print("File Name : ",fname)

if __name__ == "__main__":
    main()