import os
import pathlib
import shutil
import time
from os import path

# определение пути
startDirectory = input(r"Введите корневую директорию поиска(Например, C:\): ").strip()
outputFolder = input(r"Введите полный адрес директории, в которое будет осуществляться"
                     r" копирование(Например D:\resultFolder): ").strip()
currentDirectory = pathlib.Path(startDirectory)

# определение шаблона
PatternList = ["txt", "xls", "wav", "doc", "lgf", "mxl"]
all_files_paths = []


def recursive_search(folder_path: path):
    folders_list = []
    files_list = []
    current_directory = pathlib.Path(folder_path)
    for file in current_directory.iterdir():
        if file.is_file():
            files_list.append(file)
        elif file.is_dir():
            folders_list.append(file)
    for file in files_list:
        if str(file).split('.')[-1] in PatternList:
            all_files_paths.append(path.abspath(file))
    for directory in folders_list:
        try:
            recursive_search(path.abspath(directory))
        except Exception:
            pass


def copy_files():
    print("Идёт процесс переноса файлов...")
    for filePath in all_files_paths:
        try:
            shutil.copy(filePath, outputFolder)
        except Exception:
            pass


def main():
    print("Идёт сбор файлов...")
    start_time1 = time.time()
    recursive_search(currentDirectory)

    print("#"*50)
    print(f"Время, потраченное на сбор {len(all_files_paths)} файлов: {time.time() - start_time1} seconds")
    start_time2 = time.time()
    copy_files()
    print(f"Время, потраченное на запись {len(all_files_paths)} файлов: {time.time() - start_time2} секунд")
    print("Примечание: Системные файлы запрашивающие особые права доступа не были записаны")

    print(f"Общее время работы программы составило {time.time() - start_time1} секунд")

    os.system("PAUSE")


if __name__ == "__main__":
    main()
