from ftplib import FTP
import re

ftp = FTP()
ftp.connect("192.168.166.1", 21)  # Замените 'localhost' на IP-адрес сервера, если он на другом устройстве
ftp.login("user", "password")



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

for i in range(len(arr)):
    
# Скачивание файла
    with open(arr[i], "wb") as f:
        ftp.retrbinary(f"RETR {arr[i]}", f.write)

# # # Загрузка файла
# with open("local_file_to_upload.txt", "rb") as f:
#     ftp.storbinary("STOR remote_file.txt", f)

# Завершение сеанса
ftp.quit()
