import argparse
import concurrent.futures
import logging
from pathlib import Path
from time import time
from shutil import copyfile


"""
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

folders = []


def grabs_folder(path_folder: Path):
    """
    Функція рекурсивно обходить теку.
    """
    for el in path_folder.iterdir():
        if el.is_dir():
            folders.append(Path(el))
            logging.debug(f"Enter path = {str(el)}")
            grabs_folder(el)


def sort_file(path_folder: Path):
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
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    folders.append(base_folder)
    grabs_folder(base_folder)

    logging.debug(folders)
    time_start = time()
    logging.debug(time_start)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(sort_file, folders)
    time_finish = time()
    logging.debug(time_finish)
    logging.debug(f"time {time_finish - time_start}")


if __name__ == "__main__":
    main()
