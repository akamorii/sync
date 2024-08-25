from ftplib import FTP
import os
from config import desktop, PATH_Y

# Настройки FTP-сервера
ftp_host = "192.168.166.1"
ftp_port = 21
ftp_user = "user"
ftp_pass = "password"

# Путь к архиву на сервере, который нужно скачать
remote_file_path = PATH_Y  # Укажите точный путь на сервере

# Локальный путь, куда вы хотите сохранить скачанный файл
local_file_path = os.path.join('C:/Users/ineve/OneDrive/Рабочий стол/', 'my_archive.zip')

# Подключение к FTP-серверу
ftp = FTP()
ftp.connect(ftp_host, ftp_port)
ftp.login(ftp_user, ftp_pass)


first_index_name = 55
arr = []
# Листинг файлов на сервере
def hand_line(line):
    global arr  
    arr.append(line[first_index_name:len(line)])
    

ftp.retrlines("LIST", callback=hand_line)
# print (ftp.retrlines("LIST"))
print(arr)


# Открытие локального файла в бинарном режиме для записи
with open(local_file_path, 'wb') as file:
    # Скачивание файла с сервера
    ftp.retrbinary(f'RETR {remote_file_path}', file.write)

# Завершение сеанса
ftp.quit()

print(f'Файл {remote_file_path} успешно загружен и сохранен как {local_file_path}')
