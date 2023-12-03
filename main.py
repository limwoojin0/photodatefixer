import os
from ctypes import windll, wintypes, byref
import datetime
import time

fileLocation = "E:\\DCIM\\Download\\"
filelist = os.listdir(fileLocation)
for i in filelist:
    modTime = os.path.getmtime(fileLocation + i)
    creTime = os.path.getctime(fileLocation + i)
    mod = datetime.datetime.fromtimestamp(modTime).strftime("%Y-%m-%d %H:%M:%S")
    cre = datetime.datetime.fromtimestamp(creTime).strftime("%Y-%m-%d %H:%M:%S")
    if modTime != creTime:
        print(f"{i}\ncreation:{cre}\nmoderation:{mod}")
        answer = input()
        if answer == "c":
            timestamp = int((modTime * 10000000) + 116444736000000000)
            ctime = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)
            handle = windll.kernel32.CreateFileW(
                fileLocation + i, 256, 0, None, 3, 128, None
            )
            windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
            windll.kernel32.CloseHandle(handle)
        elif answer == "m":
            os.utime(fileLocation + i, (creTime, creTime))
        else:
            date = input("년-월-일 시:분:초")
            date = datetime.datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
            date = time.mktime(date.timetuple())
            timestamp = int((date * 10000000) + 116444736000000000)
            ctime = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)
            handle = windll.kernel32.CreateFileW(
                fileLocation + i, 256, 0, None, 3, 128, None
            )
            windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
            windll.kernel32.CloseHandle(handle)
            os.utime(fileLocation + i, (date, date))
