import os
from pathlib import Path


def find_files_by_extension(folder_path: str, extension: str):
    found_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith("." + extension):
                found_files.append(os.path.join(root, file))
    return found_files


def find_files_with_string(directory, search_string):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if search_string in f.read():
                        found_files.append(file_path)
            except UnicodeDecodeError:
                # Пропускаем файлы, которые не могут быть декодированы как UTF-8
                pass
            except Exception as e:
                print("Ошибка при чтении файла {}: {}".format(file_path, e))
    return found_files


def remove_empty_directories(directory: str):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not any(os.scandir(dir_path)):
                # Если папка пуста, удаляем её
                os.rmdir(dir_path)
                print(f"Удалена пустая папка: {dir_path}")
