from config import PATH_x, test_dst, desktop
import os
import shutil
from time import sleep
import zipfile

source_dir = PATH_x

# Указываем путь к целевой папке
destination_dir = test_dst

if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir)

# Копируем папку
shutil.copytree(source_dir, destination_dir)
# sleep(3)

def zip_directory(folder_path, zip_file_path):
    # Создание нового ZIP-архива
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Рекурсивный проход по всем файлам и подпапкам
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Получение полного пути к файлу
                file_path = os.path.join(root, file)
                # Добавление файла в архив
                # os.path.relpath делает путь относительно исходной папки
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

# if os.path.exists(destination_dir):
#     shutil.rmtree(destination_dir)      
zip_directory(test_dst,desktop)
