# command line
import sys
import os
import time
import schedule
import shutil
import hashlib

def calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            fobj.update(data)
    fobj.close()

    return hobj.hexdigest()


def BackupFiles(Source, Destination):
    Copied_Files = []
    print("Creating the Backup folder for backup process")
    
    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # copy the files if its new
            if((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                shutil.copy2(src_path, dest_path)
                Copied_Files.append(relative)

    return Copied_Files


def MarvellousDataShieldStart(Source = "Data"):
    BackupName = "MarvellousBackup"
    print("Backup Process Started Successfully at :",time.ctime())

    files = BackupFiles(Source, BackupName)

    print("Report about the backup")
    for name in files:
        print(name)

def main():
    Border = "-"*50
    print(Border)
    print("--------- Marvellous Data Shield System ----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to :")
            print("1. Takes auto backup at given time")
            print("2. Backup only new and updated files")
            print("3. Create and archive of the backup periodically")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("Scriptname.py TimeIntervel SourceDirectory")
            print("TimeInterval :  the time in minutes for periodic scheduling")
            print("SourceDirectory : Name o directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("please use --h or --u to get more details")
            
    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside Proect Logic")
        print("Time interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])

        # apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])

        print("Platform Data Sheild System started successfully")
        print("Time intervael in minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop the execuation")

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("please use --h or --u to get more details")

    print(Border)
    print("----------Thank You for using our script----------")
    print(Border)
    
if __name__ == "__main__":
    main()