import argparse
from threading import Semaphore, Thread
import logging
from pathlib import Path
from time import time
from shutil import copyfile


"""
Скрипт для сортування файлів.

Сортує за розширенням, створює теки з розширенням файлів і копіює туди файли.

Commands for script.
py main.py --source -s path_folder
py main.py --output -o result_folder
"""


parser = argparse.ArgumentParser(description='App for sorting folder')
parser.add_argument('-s', '--source', required=True)      # option that takes a value
parser.add_argument('-o', '--output', default='result_folder')
args = vars(parser.parse_args())  # object -> dict
source = args.get('source')
output = args.get('output')

base_folder = Path(source)
output_folder = Path(output)

folders = []  # list folders


def grabs_folder(path_folder: Path):
    """
    Функція збирає список тек в вхідній теці..
    """
    for el in path_folder.iterdir():
        if el.is_dir():
            folders.append(Path(el))
            logging.debug(f"Enter path = {str(el)}")
            grabs_folder(el)


def sort_file(condition, path_folder: Path):
    """
    Функція копіює файли в теку з назвою їх розширення.
    Тека за замовчуванням result_folder, зберігається там де був відкритий файл.
    """
    with condition:
        for el in path_folder.iterdir():
            if el.is_file():
                ext = el.suffix
                new_path = output_folder / ext
                try:
                    new_path.mkdir(exist_ok=True, parents=True)
                    copyfile(el, new_path / str(str(time()) + " | " + el.name))
                    logging.debug(f"File - ({el.name}) copied.")
                except OSError as e:
                    logging.error(e)


def main():
    """
    Логіка скрипта.
    """

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    folders.append(base_folder)
    grabs_folder(base_folder)

    logging.debug(folders)

    time_start = time()
    logging.debug(time_start)

    pool = Semaphore(2)
    for num in range(4):
        thread = Thread(name=f'Th-{num}', target=sort_file, args=(pool, folders))
        thread.start()

    time_finish = time()
    logging.debug(time_finish)
    logging.debug(f"time {time_finish - time_start}")


if __name__ == "__main__":
    main()
