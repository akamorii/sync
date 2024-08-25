from ftplib import FTP
import re
from config import desktop, PATH_x
import os

ftp = FTP()
ftp.connect("192.168.166.1", 21)  # Замените 'localhost' на IP-адрес сервера, если он на другом устройстве
ftp.login("user", "password")
local_file_path = 'C:/Users/ineve/OneDrive/Рабочий стол/my_archive.zip'
# remote_path = 

# def find_time(string):
#     a = re.search(r'\d{2}:\d{2}',string).group()
#     return a

first_index_name = 55
arr = []
# Листинг файлов на сервере
def hand_line(line):
    global arr  
    arr.append(line[first_index_name:len(line)])
    

ftp.retrlines("LIST", callback=hand_line)
# print (ftp.retrlines("LIST"))
print(arr)

with open(desktop, 'rb') as file:
    # Загрузка файла на сервер
    ftp.storbinary(f'STOR {PATH_x}', file)
# # # Загрузка файла
# with open("local_file_to_upload.txt", "rb") as f:
#     ftp.storbinary("STOR remote_file.txt", f)

# Завершение сеанса
ftp.quit()
