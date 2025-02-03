import os
import datetime
import re
from settings import files_directory, logs_directory, HEADERS, re_pattern
import requests
from bs4 import BeautifulSoup


def is_path_exists(pathname):
    is_exist = os.path.exists(pathname)
    return is_exist


def create_folder(pathname):
    if is_path_exists(pathname):
        save_to_logs(f"The '{pathname}' folder already exists")
    else:
        os.mkdir(pathname)
        save_to_logs(f"The '{pathname}' folder has been created")


def save_to_logs(message, is_indent=False):
    indent = ''
    if is_indent:
        indent = '\n'
    if not is_path_exists(logs_directory):
        create_folder(logs_directory)
    now = datetime.datetime.now()
    file_name = f'{now.strftime("%Y%m%d")}_log.txt'
    with open(f"{logs_directory}/{file_name}", 'a', encoding='utf-8') as file:
        file.write(f"{indent}{now.strftime('%Y-%m-%d %H:%M:%S')}: {message}\n")
    print(f"{indent}{datetime.datetime.now().strftime('%H:%M:%S')}: {message}")


def get_soup(url):
    try:
        req = requests.get(url, headers=HEADERS)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        return soup
    except Exception as e:
        save_to_logs(f"ERROR during soup getting:\n{e}")
        return False, change_to


def change_symbols(pattern_name, change_to, text):
    return re.sub(pattern_name, change_to, text)


if __name__ == '__main__':
    pass
