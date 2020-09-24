import datetime as dt
import time
import os

def del_zip(directory):
    
    for folder, subfolders, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                path = os.path.join(folder,file)
                info = os.stat(path)
                mtime = dt.datetime.fromtimestamp(info.st_mtime)
                if mtime <= (dt.datetime.now() - dt.timedelta(weeks = 4)):
                    os.remove(os.path.join(folder,file))

def main():
    
    del_zip(r'C:\Users\jcaraan\OneDrive - DXC Production\Desktop\test')

if __name__ == "__main__":
    main()